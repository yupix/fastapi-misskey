from typing import Any, Dict


async def remove_empty_dict(data: Dict[str, Any]):
    return {i: data[i] for i in data if data[i] is not None}
