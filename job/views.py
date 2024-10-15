from django.shortcuts import render,redirect,get_object_or_404

from .models import Recruiter, Seeker, HiringSeekers, RemovedPost
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'Home.html')

def login_seeker(request):

    if request.method == 'POST':
        mail = request.POST['email']
        passw = request.POST['password']

        try:
            login = Seeker.objects.get(email = mail)
            if login.psw == passw:
                return redirect('sek_home', pk = login.pk)
            else:
                messages.error(request,'Invalid Password')
        except Seeker.DoesNotExist:
            messages.error(request,"Account doesn't exist")

    return render(request,'login_seeker.html')

def login_recruiter(request):

    if request.method == 'POST':
        mail = request.POST['email']
        passw = request.POST['password']

        try:
            login = Recruiter.objects.get(email = mail)
            if login.psw == passw:
                return redirect('rec_home')
            else:
                messages.error(request,'Invalid Password')
        except Recruiter.DoesNotExist:
            messages.error(request,"Account doesn't exist")        

    return render(request,'login_recruiter.html')

def reg_seeker(request):

    if request.method == 'POST':
        fname = request.POST.get('full_name')
        pic = request.FILES.get('photo')
        email = request.POST.get('email')
        psw = request.POST.get('password')
        phno = request.POST.get('phone')
        gen = request.POST.get('gender')
        dob = request.POST.get('dob')
        add = request.POST.get('address')
        hq = request.POST.get('education')
        un = request.POST.get('university')
        sd = request.POST.get('edu_start')
        ed = request.POST.get('edu_end')
        we = request.POST.get('experience')
        pc = request.POST.get('employment')
        pjt = request.POST.get('job_type')
        pjl = request.POST.get('locations')
        atw = request.POST.get('availability')
        ks = request.POST.get('skills')
        lk = request.POST.get('languages')
        intern = request.POST.get('internships')
        proj = request.POST.get('projects')
        certi = request.POST.get('certifications')
        ps = request.POST.get('profile_summary')
        resume = request.FILES.get('resume')
        # print(fname,pic,email,psw,phno,gen,dob,add,hq,un,sd,ed,we,pc,pjt,pjl,atw,ks,lk,intern,proj,certi,ps,resume)

        sek = Seeker.objects.create(fname=fname,pic=pic,email=email,psw=psw,phno=phno,gen=gen,dob=dob,add=add,hq=hq,un=un,sd=sd,ed=ed,we=we,pc=pc,pjt=pjt,pjl=pjl,atw=atw,ks=ks,lk=lk,intern=intern,proj=proj,certi=certi,ps=ps,resume=resume)
        sek.save()
        print('done')
        return redirect('login_seeker')

    return render(request,'reg_seeker.html')

def reg_recruiter(request):

    if request.method == 'POST':
        cname = request.POST.get('company_name')
        fname = request.POST.get('recruiter_name')
        email = request.POST.get('email')
        phno = request.POST.get('phone')
        psw = request.POST.get('password')
        webs = request.POST.get('website')
        lp = request.POST.get('linkedin')
        loc = request.POST.get('location')
        au = request.POST.get('about_us')
        ind = request.POST.get('industry')
        wwo = request.POST.get('what_we_offer')
        # print(cname,fname,email,phno,psw,webs,lp,loc,au,ind,wwo)

        rec = Recruiter.objects.create(cname=cname,fname=fname,email=email,phno=phno,psw=psw,webs=webs,lp=lp,loc=loc,au=au,ind=ind,wwo=wwo)
        rec.save()
        print('success')
        return redirect('login_recruiter')
        
    return render(request,'reg_recruiter.html')

def recruiter_home(request):

    openings = HiringSeekers.objects.all().order_by('-id')

    context = {
        'openings':openings
    }

    return render(request,'recruiter_home.html',context)

def seeker_home(request,pk):
    # pk = 1
    details = Seeker.objects.get(id = pk)
    jobpost = HiringSeekers.objects.all()

    context = {
        'details':details,
        'jobpost':jobpost
    }

    return render(request,'seeker_home.html',context)

def hiring_seekers(request):

    if request.method == 'POST':
        jt = request.POST.get('job_title')
        cn = request.POST.get('company_name')
        jl = request.POST.get('job_location')
        cl = request.FILES.get('company_logo')
        jtyp = request.POST.get('job_type')
        er = request.POST.get('education')
        kysk = request.POST.get('key_skills')
        exp = request.POST.get('experience')
        abtcomp = request.POST.get('about_company')
        pos = request.POST.get('job_openings')
        jd = request.POST.get('job_description')
        jr = request.POST.get('job_requirements')
        sal = request.POST.get('salary')
        al = request.POST.get('apply_link')
        ld = request.POST.get('last_date')
        # print(jt,cn,jl,cl,jtyp,er,kysk,exp,abtcomp,pos,jd,jr,sal,al,ld)

        hirsek = HiringSeekers.objects.create(jt=jt,cn=cn,jl=jl,cl=cl,jtyp=jtyp,er=er,kysk=kysk,exp=exp,abtcomp=abtcomp,pos=pos,jd=jd,jr=jr,sal=sal,al=al,ld=ld)
        # hirsek.save()
        print('complete')

        return redirect('rec_home')
      
    return render(request,'hiring_seekers.html')


def view_job_post(request,pk):

    # pk = 4
    hirsek = get_object_or_404(HiringSeekers,id = pk)

    context = {
        'hirsek':hirsek
    }

    return render(request,'view_job_post.html',context)


def removed_post(request,pk):

    remov = get_object_or_404(HiringSeekers, id = pk)

    RemovedPost.objects.create(
        jt = remov.jt,
        cn = remov.cn,
        jl = remov.jl,
        cl = remov.cl,
        jtyp = remov.jtyp,
        er = remov.er,
        kysk = remov.kysk,
        exp = remov.exp,
        abtcomp = remov.abtcomp,
        pos = remov.pos,
        jd = remov.jd,
        jr = remov.jr,
        sal = remov.sal,
        al = remov.al,
        ld = remov.ld
    )
    remov.delete()
    return redirect('jp_history')

def jobpost_history(request):

    remov_post = RemovedPost.objects.all().order_by('-id')

    context = {
        'remov_post':remov_post
    }

    return render(request,'job_post_history.html',context)

def edit_profile(request,pk):
    # pk = 1
    edit = Seeker.objects.get(id = pk)

    if request.method == 'POST':
        edit.fname = request.POST.get('full_name')
        edit.pic = request.FILES.get('photo')
        edit.email = request.POST.get('email')
        edit.psw = request.POST.get('password')
        edit.phno = request.POST.get('phone')
        edit.gen = request.POST.get('gender')
        edit.dob = request.POST.get('dob')
        edit.add = request.POST.get('address')
        edit.hq = request.POST.get('education')
        edit.un = request.POST.get('university')
        edit.sd = request.POST.get('edu_start')
        edit.ed = request.POST.get('edu_end')
        edit.we = request.POST.get('experience')
        edit.pc = request.POST.get('')
    context = {
        'edit':edit
    }
    return render(request,'edit_reg_seeker.html',context)