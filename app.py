from flask import Flask, render_template, request

from linklist_ans import LinkedList
app = Flask(__name__)

my_list = LinkedList()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)


@app.route('/works/circle', methods=['GET', 'POST'])
def acircle():
    result = None
    if request.method == 'POST':
        radius = request.form.get('radius', '')
        result = int(radius)*3.14*int(radius)
    return render_template('circle.html', result=result)

@app.route('/works/triangle', methods=['GET', 'POST'])
def atriangle():
    result = None
    if request.method == 'POST':
        base = request.form.get('base', '')
        height = request.form.get('height', '')
        if base and height:
            result = 0.5 * float(base) * float(height)
    return render_template('triangle.html', result=result)

@app.route('/works/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        text = request.form.get('text', '')
        result = text.upper()
    return render_template('touppercase.html', result=result)

linked_list_elements = []

@app.route('/works/linkedlist', methods=['GET', 'POST'])
def linkedlist_ui():
    message = None
    search_result = None
    
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'insert_end':
            val = request.form.get('value')
            if val:
                my_list.insert_at_end(val)
                message = f"Inserted '{val}' at the end."
                
        elif action == 'insert_beginning':
            val = request.form.get('value')
            if val:
                my_list.insert_at_beginning(val)
                message = f"Inserted '{val}' at the beginning."
                
        elif action == 'insert_after':
            target = request.form.get('target_value')
            val = request.form.get('value')
            if target and val:
                result = my_list.insert_after(target, val)
                if result:
                    message = f"Inserted '{val}' after '{target}'."
                else:
                    message = f"Target node '{target}' not found."
                    
        elif action == 'remove_beginning':
            removed = my_list.remove_beginning()
            message = f"Removed '{removed}' from the beginning." if removed is not None else "List is empty."
            
        elif action == 'remove_end':
            removed = my_list.remove_at_end()
            message = f"Removed '{removed}' from the end." if removed is not None else "List is empty."
            
        elif action == 'remove_value':
            val = request.form.get('value')
            if val:
                removed = my_list.remove_at(val)
                message = f"Removed '{removed}' from the list." if removed is not None else f"Value '{val}' not found."
                
        elif action == 'search':
            val = request.form.get('value')
            if val:
                found = my_list.search(val)
                search_result = f"Value '{val}' was {'found' if found else 'not found'} in the list."

    elements = []
    curr = my_list.head
    while curr:
        elements.append(curr.data)
        curr = curr.next

    return render_template('linkedlist.html', elements=elements, message=message, search_result=search_result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
