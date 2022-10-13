"""
Created on Mon Apr 11 14:07:19 2022

@author: Band of Brothers
"""
    import PyPDF2 as reader
    #import textract
    import re
    import string
    import pandas as pd
    import matplotlib.pyplot as plt


    pdf = open('resume.pdf','rb')     #open pdf

    pdfReader = reader.PdfFileReader(pdf)          #read file

    num_pages = pdfReader.numPages   #total nuumber of pages

    count = 0           # Initialize a count for the number of pages


    extractedtext = ""            # Initialize a text empty etring variable


    while count < num_pages:          # Extract text from every page on the file
        pageObj = pdfReader.getPage(count)
        count +=1
        extractedtext += pageObj.extractText()


    extractedtext = extractedtext.lower()

    extractedtext = re.sub(r'\d+','',extractedtext) #removenumbers

    extractedtext = extractedtext.translate(str.maketrans('','',string.punctuation)) #remove puctuation


    terms = {'Quality/Six Sigma':['black belt','capability analysis','control charts','doe','dmaic','fishbone',             #Create dictionary with industrial and system engineering key terms by area
                                  'gage r&r', 'green belt','ishikawa','iso','kaizen','kpi','lean','metrics',
                                  'pdsa','performance improvement','process improvement','quality',
                                  'quality circles','quality tools','root cause','six sigma',
                                  'stability analysis','statistical analysis','tqm'],
            'Operations management':['automation','bottleneck','constraints','cycle time','efficiency','fmea',
                                     'machinery','maintenance','manufacture','line balancing','oee','operations',
                                     'operations research','optimization','overall equipment effectiveness',
                                     'pfmea','process','process mapping','production','resources','safety',
                                     'stoppage','value stream mapping','utilization','python'],
            'Supply chain':['abc analysis','apics','customer','customs','delivery','distribution','eoq','epq',
                            'fleet','forecast','inventory','logistic','materials','outsourcing','procurement',
                            'reorder point','rout','safety stock','scheduling','shipping','stock','suppliers',
                            'third party logistics','transport','transportation','traffic','supply chain',
                            'vendor','warehouse','wip','work in progress'],
            'Project management':['administration','agile','budget','cost','direction','feasibility analysis',
                                  'finance','kanban','leader','leadership','management','milestones','planning',
                                  'pmi','pmp','problem','project','risk','schedule','scrum','stakeholders',"project"],
            'Data analytics':['analytics','api','aws','big data','busines intelligence','clustering','code',
                              'coding','data','database','data mining','data science','deep learning','hadoop',
                              'hypothesis test','iot','internet','machine learning','modeling','nosql','nlp',
                              'predictive','programming','python','r','sql','tableau','text mining',
                              'visualuzation'],

            'Healthcare':['adverse events','care','clinic','cphq','ergonomics','healthcare',
                          'health care','health','hospital','human factors','medical','near misses',
                          'patient','reporting system'],
            "Education and Training":["administration","assisted","awarded","classroom","coach","course","discipline","education","training","interactive","networking","mentor","tutoring","training"],

              "Law Enforcement":["clerk","copyrightlaw","joint venture","legal recearch","trial law","will preparation"],

              "Tourism and Hospitality":["budgeting","catering","flexibility","customer service","greeting","maintenance","marketing","positivity","server","travel","tourism","transportation"],

              "Marketing and Business":["account management","agile","analytical","analyzing data","branding","automation","budget management","business plans","business strategy","business system","client relationships","coding","counseling","data analysis","data management","six sigma","supply chain management"] }


    quality = 0
    operations = 0
    supplychain = 0
    project = 0
    data = 0
    healthcare = 0                                #Initialize scores variables
    education= 0
    law = 0
    tourism = 0
    marketing = 0
    finance = 0
    architecture = 0



    scores = []

    # Obtain the scores for each area
    for region in terms.keys():

        if region == 'Quality/Six Sigma':
            for word in terms[region]:
                if word in extractedtext:
                    quality +=1
            scores.append(quality)

        elif region == 'Operations management':
            for word in terms[region]:
                if word in extractedtext:
                    operations +=1
            scores.append(operations)

        elif region == 'Supply chain':
            for word in terms[region]:
                if word in extractedtext:
                    supplychain +=1
            scores.append(supplychain)

        elif region == 'Project management':
            for word in terms[region]:
                if word in extractedtext:
                    project +=1
            scores.append(project)

        elif region == 'Data analytics':
            for word in terms[region]:
                if word in extractedtext:
                    data +=1
            scores.append(data)

        elif region == "Education and Training":
            for word in terms[region]:
                if word in extractedtext:
                    education +=1
                    scores.append(education)

        elif region == "Law enforcement":
            for word in terms[region]:
                if word in extractedtext:
                    law +=1
                    scores.append(law)

        elif region == "Tourism and Hospitality":
             for word in terms[region]:
                 if word in extractedtext:
                     tourism +=1
                     scores.append(tourism)

        elif region == "Marketing and Business":
            for word in terms[region]:
                if word in extractedtext:
                    marketing+=1
                    scores.append(marketing)

        else:
            for word in terms[region]:
                if word in extractedtext:
                    healthcare +=1
            scores.append(healthcare)


    summary = pd.DataFrame(scores,index=terms.keys(),columns=['score']).sort_values(by='score',ascending=False)            # Creates a data frame with scores
    summary


    pie = plt.figure(figsize=(11,11))
    plt.pie(summary['score'], labels=summary.index, explode = None, autopct='%1.0f%%',shadow=True,startangle=90)
    plt.title('Job Recommendation\n\n')                                                                                        # Creates a pie chart
    plt.axis('equal')
    plt.show()

    # Save pie chart as a .png file
    pie.savefig('resume_screening_results.png',dpi = 1920*1080)

 
