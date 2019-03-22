from django.shortcuts import render
import requests
import json

def home(request):
	url="https://newsapi.org/v2/top-headlines?country=in&apiKey=89aa79ae8ccb4fabbc83f1a572eaa445"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def world(request):
	url="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=89aa79ae8ccb4fabbc83f1a572eaa445"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def sports(request):
	url="https://newsapi.org/v2/top-headlines?category=sports&apiKey=89aa79ae8ccb4fabbc83f1a572eaa445&country=in"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def entertainment(request):
	url="https://newsapi.org/v2/top-headlines?category=entertainment&apiKey=89aa79ae8ccb4fabbc83f1a572eaa445&country=in"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def business(request):
	url="https://newsapi.org/v2/top-headlines?category=business&apiKey=89aa79ae8ccb4fabbc83f1a572eaa445&country=in"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def science(request):
	url="https://newsapi.org/v2/top-headlines?category=science&apiKey=89aa79ae8ccb4fabbc83f1a572eaa445&country=in"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def tech(request):
	url="https://newsapi.org/v2/top-headlines?category=technology&apiKey=89aa79ae8ccb4fabbc83f1a572eaa445&country=in"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def search(request):
	keyword=""
	if request.method=='POST':
		keyword=request.POST['keyword']
	url="https://newsapi.org/v2/everything?q="+keyword+"&apiKey=89aa79ae8ccb4fabbc83f1a572eaa445&language=en&sortBy=relevance"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api,'keyword':keyword})

def about(request):
	return render(request,'about.html',{})

def convert(request):
	return render(request,'convert.html',{})

def convert_json(request):
	url="http://www.google.com"
	if request.method=="POST":
		url=request.POST["url"]

	try:
		r=requests.get(url)
	except:
		dic={"status_code":404,"message":"Error in url.Please check your url","count":0}
		res_str=json.dumps(dic)
		result=json.loads(res_str)
		if "_convert" in request.POST:
			return render(request,'convert_json.html',{"result":res_str})
		else:
			return render(request,'form_layout.html',{"result":result})

	if r.status_code!=200:
	    dic={"status_code":r.status_code,"message":requests.status_codes._codes[r.status_code][0],"count":0}
	    res_str=json.dumps(dic)
	    result=json.loads(res_str)
	    if "_convert" in request.POST:
	    	return render(request,'convert_json.html',{"result":res_str})
	    else:
	    	return render(request,'form_layout.html',{"result":result})

	from bs4 import BeautifulSoup    
	soup=BeautifulSoup(r.content,'html.parser')

	form_elem=soup.find_all('form',id='mG61Hd')
	if len(form_elem)==0:
	    dic={"status_code":r.status_code,"message":"Not a google form url, please enter valid url.","count":0}
	    res_str=json.dumps(dic)
	    result=json.loads(res_str)
	    if "_convert" in request.POST:
	    	return render(request,'convert_json.html',{"result":res_str})
	    else:
	    	return render(request,'form_layout.html',{"result":result})

	link=form_elem[0]["action"]
	title=soup.find('div',class_='freebirdFormviewerViewHeaderTitleRow').text
	description=soup.find('div',class_='freebirdFormviewerViewHeaderDescription').text

	qsoup=soup.find('div',class_="freebirdFormviewerViewItemList")
	arr=qsoup.find_all('div',recursive=False)

	num=len(arr)

	questions=[]

	q_container="freebirdFormviewerViewNumberedItemContainer"
	radio_group="freebirdFormviewerViewItemsItemItem"
	text_type="freebirdFormviewerViewItemsTextTextItem"
	text_area_type=""

	for question in arr:
	    
	    qtype=""
	    text=""
	    img_url=""
	    options=[]
	    name=""
	    required="false"

	    if question["class"][0]==q_container:
	        question=question.find('div',recursive=False)

	    dict_att=question.attrs
	    if "data-required" in dict_att:
	        	required=str(dict_att["data-required"])
	    else :
	        	required="false"
	        
	    d_class_list=question["class"]
	    f1=False
	    f2=False
	    for k in d_class_list:
	        if k in text_type:
	            f1=True
	        if k in radio_group:
	            f2=True
	        
	    
	    if (f1 and f2):
	        qtype="text"
	        header=question.find('div',class_="freebirdFormviewerViewItemsItemItemHeader")
	        header=header.find('div',class_="freebirdFormviewerViewItemsItemItemTitleContainer")
	        text=header.find('div',class_="freebirdFormviewerViewItemsItemItemTitle exportItemTitle freebirdCustomFont").text
	        header=question.find_all('div',class_="freebirdFormviewerViewItemsEmbeddedobjectLeft")
	        if len(header)>0:
	            img_tag=header[0].find('img')
	            img_url=img_tag["src"]
	            
	        input_tag=question.find('input')
	        name=input_tag["name"]

	        

	    elif (f2):
	        qtype="radio_group"
	        header=question.find('div',class_="freebirdFormviewerViewItemsItemItemHeader")
	        header=header.find('div',class_="freebirdFormviewerViewItemsItemItemTitleContainer")
	        text=header.find('div',class_="freebirdFormviewerViewItemsItemItemTitle exportItemTitle freebirdCustomFont").text
	        header=question.find_all('div',class_="freebirdFormviewerViewItemsEmbeddedobjectLeft")
	        if len(header)>0:
	            img_tag=header[0].find('img')
	            img_url=img_tag["src"]

	        input_div=""
	        if img_url=="":
	            input_div=question.find_all('div',recursive=False)[1]
	        else:
	            input_div=question.find_all('div',recursive=False)[2]

	        input_tag=input_div.find('input',recursive=False)
	        content_div=input_div.find('content')
	        text_options=content_div.find_all('div',class_="freebirdFormviewerViewItemsRadioOptionContainer")
	        for option in text_options:
	            o_img=option.find_all('img')
	            if len(o_img)==0:
	                o_img_url=""
	            else:
	                o_img_url=o_img[0]["src"]
	            o_text=option.text
	            options.append({"text":o_text,"img_url":o_img_url})
	        
	        name=input_tag["name"]   

	    else:
	        qtype="unknown"

	    questions.append({"type":qtype,"required":required,"text":text,"img":img_url,"name":name,"options":options})

	dic={"status_code":r.status_code,"responseLink":link,"title":title,"description":description,"count":num,"questions":questions}
	res_str=json.dumps(dic)
	result=json.loads(res_str)
	if "_convert" in request.POST:
	    return render(request,'convert_json.html',{"result":res_str})
	else:
	    return render(request,'form_layout.html',{"result":result})
