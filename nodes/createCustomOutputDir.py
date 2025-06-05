import json
import math
import os
import subprocess
import logging
import datetime
import folder_paths as comfy_paths
from comfy.comfy_types.node_typing import IO

class CreateCustomOutputDir:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": { 
                "dir_name": (IO.STRING, {"default": "project_123", }),
                "timestamp_postfix": (IO.BOOLEAN, {"default": True}),
            },
        }

    RETURN_TYPES = (IO.STRING,)
    RETURN_NAMES = ("output_path",)
    FUNCTION = "createCustomOutputDir"
    OUTPUT_NODE = True
    CATEGORY = "🔥FFmpeg"
  
    def createCustomOutputDir(self, dir_name, timestamp_postfix):
        try:
            output_path = os.path.join(comfy_paths.get_output_directory(), dir_name)
            if timestamp_postfix:
                output_path = os.path.join(output_path, datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
            os.makedirs(output_path, exist_ok=True)
            logging.info(f"[ FFMpeg Utils ] Makedir: {output_path}")
            return output_path,
        except Exception as e:
            raise ValueError(e)