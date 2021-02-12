import sys

print(sys.builtin_module_names, '\n')
print(sys.version, '\n')

# Error messages

sys.stderr.write('ERROR MESSAGE\n')
sys.stderr.flush()  # forces write to terminal
sys.stdout.write('STDOUT MESSAGE\n')
print()

# Passing arguments

print(sys.argv)
if len(sys.argv) > 1:
    print(sys.argv[1])
    
# running python sys_module.py 'Hello' will pass 'Hello into the program

sys.argv[0]