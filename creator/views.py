from django.shortcuts import render
from .models import Llm  # Import the Llm model
import llm

def index(request):
    llm_response = ""
    
    # Retrieve the model name from the database
    try:
        llm_model = Llm.objects.first()  # Get the first entry in the Llm table
        model_name = llm_model.name if llm_model else "orca-mini-3b"  # Use a default name if no entry exists
    except Llm.DoesNotExist:
        model_name = "orca-mini-3b"  # Default model name

    if request.method == 'POST':
        model = llm.get_model(model_name)  # Use the model name from the database
        llm_response = model.prompt(request.POST.get('prompt')).text()

    return render(request, 'index.html', {'llm_response': llm_response})
