import subprocess

class GPUEngineWrapper:
    """
    The Muscle: Interfaces directly with the underlying compiled C/CUDA engine 
    (like BitCrack) via subprocess, keeping the Python loop non-blocking.
    """
    def __init__(self, engine_binary_path="bin/bitcrack"):
        self.engine_path = engine_binary_path

    def run_chunk(self, address, start_hex, end_hex):
        """
        Constructs the command line arguments and executes the GPU run.
        """
        cmd = [
            self.engine_path,
            "-b", "896",           # Example BitCrack arguments for GPU blocks
            "-t", "256",           # Example BitCrack arguments for GPU threads
            "--keyspace", f"{start_hex}:{end_hex}",
            address
        ]

        try:
            # We run this process and wait for it to complete the chunk
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if "Address match found" in result.stdout:
                return {"status": "FOUND", "log": result.stdout}
            
            return {"status": "EXHAUSTED", "log": None}
            
        except FileNotFoundError:
            return {"status": "ERROR", "log": "GPU Engine binary not found."}
