from langgraph.checkpoint.memory import MemorySaver
from langgraph.checkpoint.base import Checkpoint, CheckpointMetadata
from langchain_core.load.dump import dumps
from .storage_client.supabase import supabase
import json


class MemoryManager(MemorySaver):
    def __init__(self):
        super().__init__()

    def put(
        self,
        config: dict,
        checkpoint: Checkpoint,
        metadata: CheckpointMetadata,
        new_versions: dict,
    ) -> dict:
        res_config = super().put(config, checkpoint, metadata, new_versions)
        thread_id = config.get("configurable", {}).get("thread_id")
        values = checkpoint.get("channel_values", {})

        if "messages" not in values:
            return res_config

        serialized_values = json.loads(dumps(values))

        supabase.table("chats").upsert(
            {"id": thread_id, "state": serialized_values}, on_conflict="id"
        ).execute()

        return res_config
