from django.http import HttpResponse
import os
from supabase import create_client, Client
from dotenv import load_dotenv
from django.shortcuts import render
from django.template import loader

# Load environment variables
load_dotenv()

# Initialize Supabase client
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def fetch_albums(request):
    template = loader.get_template('index.html')
    # Fetch data from the 'albums' table
    response = supabase.table('albums').select('*').execute()
    data = response.data

    #if response.status_code == 200:
        # Pass the data to the template as context
    context = {'albums': data}
        
    return HttpResponse(template.render(context, request))
    #else:
    #   return render(request, 'index.html', {'error': 'Failed to fetch data'})


