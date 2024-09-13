import xlwings as xw

# Define a function to be called from Excel
@xw.func
def hello(name):
    return f"Hello, {name}!"

# Add a macro that can be run from Excel
@xw.sub
def say_hello():
    name = xw.Range('Sheet1', 'A1').value
    message = hello(name)
    xw.Range('Sheet1', 'B1').value = message

# Run the macro when the script is executed
if __name__ == '__main__':
    xw.Book('addin.xlsm').set_mock_caller()
    say_hello()