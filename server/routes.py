from flask import Blueprint, request, jsonify, session
from models import db, JournalEntry

resource_bp = Blueprint('resource', __name__)

@resource_bp.route('/entries', methods=['GET'])
def get_entries():
    user_id = session.get('user_id')  # Ensure user is authenticated
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    entries = JournalEntry.query.filter_by(user_id=user_id).paginate(page, per_page, error_out=False)
    
    response = {
        "page": entries.page,
        "per_page": entries.per_page,
        "total": entries.total,
        "total_pages": entries.pages,
        "items": [{"id": e.id, "title": e.title, "content": e.content} for e in entries.items]
    }
    
    return jsonify(response)

@resource_bp.route('/entries', methods=['POST'])
def create_entry():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    entry = JournalEntry(title=data['title'], content=data['content'], user_id=user_id)
    db.session.add(entry)
    db.session.commit()
    return jsonify({"message": "Entry created"}), 201

@resource_bp.route('/entries/<int:id>', methods=['PATCH'])
def update_entry(id):
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    entry = JournalEntry.query.filter_by(id=id, user_id=user_id).first()
    if not entry:
        return jsonify({"error": "Entry not found"}), 404

    data = request.json
    entry.title = data.get('title', entry.title)
    entry.content = data.get('content', entry.content)
    db.session.commit()
    return jsonify({"message": "Entry updated"}), 200

@resource_bp.route('/entries/<int:id>', methods=['DELETE'])
def delete_entry(id):
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    entry = JournalEntry.query.filter_by(id=id, user_id=user_id).first()
    if not entry:
        return jsonify({"error": "Entry not found"}), 404

    db.session.delete(entry)
    db.session.commit()
    return jsonify({"message": "Entry deleted"}), 200