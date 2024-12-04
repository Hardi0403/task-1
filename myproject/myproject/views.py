from django.http import HttpResponse

def shadow_sentence(request):
    if request.method == 'POST':
        character_length = int(request.POST.get('character_length', 0))

        if character_length <= 0:
            return HttpResponse("Character length must be a positive integer.")

        sentence = request.POST.get('sentence', '')

        # Split the sentence into words and create the shadow sentence
        shadow_words = [word[0] * character_length for word in sentence.split()]
        shadow_sentence = ' '.join(shadow_words)

        return HttpResponse(shadow_sentence)

    return render(request, 'shadow_form.html')