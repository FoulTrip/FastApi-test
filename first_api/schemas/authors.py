def authorEntity(details) -> dict:
    return {
        "id": str(details["_id"]),
        "author": details["author"],
        "content": details["content"],
    }
    
def authorsEntity(entity) -> list:
    return [authorEntity(details) for details in entity]