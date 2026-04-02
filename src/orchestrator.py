import json
import os

class Orchestrator:
    """
    The Brain: Parses target ranges and yields sequential hexadecimal chunks 
    for the GPU engine to process.
    """
    def __init__(self, config_path="config/targets.json"):
        self.targets = self._load_config(config_path)

    def _load_config(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"[ERROR] Configuration file not found at {path}")
        with open(path, 'r') as f:
            return json.load(f).get("puzzles", {})

    def calculate_chunks(self, target_id, resume_hex=None):
        """
        Yields start and end hex boundaries for the GPU.
        If a crash occurred, resume_hex allows instant recovery.
        """
        if str(target_id) not in self.targets:
            raise ValueError(f"[ERROR] Target {target_id} not found in configuration.")

        target = self.targets[str(target_id)]
        start_int = int(resume_hex or target["range_start"], 16)
        end_int = int(target["range_end"], 16)
        chunk_size = target.get("chunk_size", 10000000000)

        current_int = start_int

        while current_int <= end_int:
            next_int = current_int + chunk_size
            
            # Ensure we don't overshoot the final boundary
            if next_int > end_int:
                next_int = end_int

            yield (hex(current_int)[2:], hex(next_int)[2:])
            current_int = next_int + 1

if __name__ == "__main__":
    # Quick Test of the Logic
    brain = Orchestrator()
    print("Testing chunk generation for Puzzle 67...")
    chunk_generator = brain.calculate_chunks(67)
    
    # Print the first 3 chunks to verify the math
    for _ in range(3):
        print(next(chunk_generator))
      
