from django.shortcuts import render


def index(request):

    return render(request,'index.html')
def process(request):
    #getting the text
    mytext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    capitalize = request.POST.get('capitalize','off')
    decapitalize = request.POST.get('decapitalize','off')
    remspace = request.POST.get('remspace','off')
    remnewline = request.POST.get('remnewline','off')
    remnums = request.POST.get('remnums','off')
    ccount = request.POST.get('ccount','off')
    cword = request.POST.get('cword','off')
    flag=0
    if capitalize == 'on':
        prstext = ""
        flag = flag + 1
        for char in mytext:
            prstext = prstext + char.upper()

        mytext = prstext
    if removepunc == 'on':
        p1 = ""
        flag = flag +1
        punctuations = '''!()-[]{};:'"\,./?@#$%^&*_~'''

        for char in mytext:
            if char not in punctuations:
                p1 = p1 + char
        mytext = p1
    if decapitalize == 'on':
        p2 = ""
        flag = flag + 1
        for char in mytext:
            p2 = p2 + char.lower()
        mytext = p2
    if remspace == 'on' :
        p3 = ''
        flag = flag + 1
        for char in mytext:
            if char != " ":
                p3 = p3 + char
        mytext = p3
    if remnewline == 'on' :
        p4=''
        flag = flag + 1
        for char in mytext:
            if char != '\n' and char != '\r':
                p4 = p4 + char
        mytext = p4
    if remnums=='on':
        flag= flag +1
        p5=""
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        for i in mytext:
            if i not in nums:
                p5 = p5 + i
        mytext = p5
    if ccount == 'on' and cword == 'on':
        flag = flag + 1
        if len(mytext) != 1 and len(mytext.split()) != 1:
            mytext = "{} characters and {} words in your text.".format(len(mytext),len(mytext.split()))
        elif len(mytext) == 1:
            mytext = "{} character and {} word in your text.".format(1,1)
        else:
            mytext ="{} characters and {} word in your text.".format(len(mytext), len(mytext.split()))
    elif ccount=='on':
        flag=flag+1
        if(len(mytext)==1):
            mytext = "{} character in your text.".format(len(mytext))
        else:
            mytext = "{} characters in your text.".format(len(mytext))
    elif cword=='on':
        flag = flag +1
        if(len(mytext.split())==1):
            mytext ="{} word in your text.".format(len(mytext.split()))
        else:
            mytext = "{} words in your text.".format(len(mytext.split()))
    if flag==0:
        return render(request,'def.html')
    else:
        params = {'processed_text': mytext}
        return render(request, 'processtext.html', params)
