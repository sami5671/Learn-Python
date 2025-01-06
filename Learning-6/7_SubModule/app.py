import subprocess

result = subprocess.run(
    ["node", '-v'],
    capture_output=True,
    text=True
)

print(result.stdout) 