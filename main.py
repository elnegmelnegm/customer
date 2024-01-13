import streamlit as st

# Display header
st.set_page_config(
    page_title="ُEDA centre",
    page_icon="https://www.edaegypt.gov.eg/media/wc3lsydo/group-287.png",
    layout="wide",
)



st.markdown('''
<img src="https://www.edaegypt.gov.eg/media/wc3lsydo/group-287.png" width="250" height="100">''', unsafe_allow_html=True)
st.title ("EDA trusted Center")
st.markdown('''
     ''', unsafe_allow_html=True)
#st.video("https://pixabay.com/en/videos/star-long-exposure-starry-sky-sky-6962/")


st.link_button("للاستفسار عن معلومات دوائية موثوقة", "https://edaegypt.gov.eg/ar/%D8%A7%D9%84%D8%AE%D8%AF%D9%85%D8%A7%D8%AA/%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D9%81%D8%B3%D8%A7%D8%B1-%D8%B9%D9%86-%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A7%D8%AA-%D8%AF%D9%88%D8%A7%D8%A6%D9%8A%D8%A9-%D9%85%D9%88%D8%AB%D9%88%D9%82%D8%A9/", use_container_width= True, help="تتيح هذه الخدمة للمواطن إمكانية طلب استشارة دوائية أو الاستفسار عن اي معلومة تتعلق بالأدوية والمستحضرات الصيدلية؛ حيث يقوم فريق متخصص من مركز المعلومات الدوائية المصري التابع  للإدارة المركزية للرعاية الصيدلية بهيئة الدواء المصرية بالرد على كافة الاستفسارات الواردة، وتقديم المعلومة الدوائية باستخدام أسلوب منهجي وفقًا لحالة كل مستفسر")
st.link_button("الاستفسار عن توافر المستحضرات الدوائية", "https://edaegypt.gov.eg/ar/%D8%A7%D9%84%D8%AE%D8%AF%D9%85%D8%A7%D8%AA/%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D9%81%D8%B3%D8%A7%D8%B1-%D8%B9%D9%86-%D8%AA%D9%88%D8%A7%D9%81%D8%B1-%D8%A7%D9%84%D9%85%D8%B3%D8%AA%D8%AD%D8%B6%D8%B1%D8%A7%D8%AA-%D8%A7%D9%84%D8%AF%D9%88%D8%A7%D8%A6%D9%8A%D8%A9/", use_container_width= True, help="تتيح الخدمة لكافة المواطنين الاستفسار عن مدى توافر المستحضرات الدوائية في السوق الدوائي المصري، ومن ثم تقوم الإدارة المعنية بهيئة الدواء المصرية بالتواصل مع مقدم الاستفسار للإجابة على الاستفسار المقدم، وكذلك يمكنكم التواصل معنا مباشرة على الخط الساخن 15301")

st.link_button("لمتابعة المنشورات الصادرة من هيئة الدواء", "https://app.powerbi.com/view?r=eyJrIjoiZDNmZDU0NDEtZmE0ZC00NmQyLTk5MWItNjNjMGY4NTgyOGEzIiwidCI6ImUxNjE5YjA3LTAxMjAtNGRmOS04NjZkLTNhNjA0MDVjMmMxNCJ9&pageName=ReportSection", use_container_width= True,help="تتيح هذه الخدمة للمواطن إمكانية تتبع المنشورات الصادرة من هيئة الدواء المصرية التي تصدر بشكل دوري ")
st.link_button("للإبلاغ عن المواد الدعائية الدوائية الغير ملائمة ", "https://edaegypt.gov.eg/ar/%D8%A7%D9%84%D8%AE%D8%AF%D9%85%D8%A7%D8%AA/%D8%A7%D9%84%D8%A5%D8%A8%D9%84%D8%A7%D8%BA-%D8%B9%D9%86-%D9%85%D9%88%D8%A7%D8%AF-%D8%AF%D8%B9%D8%A7%D8%A6%D9%8A%D8%A9-%D8%AF%D9%88%D8%A7%D8%A6%D9%8A%D8%A9-%D8%BA%D9%8A%D8%B1-%D9%85%D9%84%D8%A7%D8%A6%D9%85%D8%A9/", use_container_width= True,help="تتيح هذه الخدمة للمواطنين إمكانية الإبلاغ عن المخالفات المتعلقة بمواد التسويق والإعلان الدوائي ")

st.link_button("الإبلاغ عن الآثار الجانبية للمستحضرات والمستلزمات الطبية", "https://edaegypt.gov.eg/ar/%D8%A7%D9%84%D8%AE%D8%AF%D9%85%D8%A7%D8%AA/%D8%A7%D9%84%D8%A5%D8%A8%D9%84%D8%A7%D8%BA-%D8%B9%D9%86-%D8%A7%D9%84%D8%A2%D8%AB%D8%A7%D8%B1-%D8%A7%D9%84%D8%AC%D8%A7%D9%86%D8%A8%D9%8A%D8%A9/", use_container_width= True,help=" تتيح هذه الخدمة للمواطن إمكانية الإبلاغ عن الآثار الجانبية للأدوية أو المستحضرات الحيوية واللقاحات أو مستحضرات التجميل أو المستلزمات الطبية ")

st.link_button("الإبلاغ عن مخالفات تخص المستحضرات أو المنشآت الصيدلية", "https://edaegypt.gov.eg/ar/%D8%A7%D9%84%D8%AE%D8%AF%D9%85%D8%A7%D8%AA/%D8%A7%D9%84%D8%A5%D8%A8%D9%84%D8%A7%D8%BA-%D8%B9%D9%86-%D9%85%D8%AE%D8%A7%D9%84%D9%81%D8%A7%D8%AA/", use_container_width= True,help="للإبلاغ عن أية مخالفات تصدر عن المؤسسات الصيدلية وتداول المستحضرات الصيدلية وجودتها")



st.title ("EDA AI Center")
st.markdown('''
Powered by Google AI <img src="https://seeklogo.com/images/G/google-ai-logo-996E85F6FD-seeklogo.com.png" width="20" height="20"> Streamlit <img src="https://global.discourse-cdn.com/business7/uploads/streamlit/original/2X/f/f0d0d26db1f2d99da8472951c60e5a1b782eb6fe.png" width="22" height="22"> Python <img src="https://i.ibb.co/wwCs096/nn-1-removebg-preview-removebg-preview.png" width="22" height="22">''', unsafe_allow_html=True)
st.markdown('''
  يعتمد التطبيق على الذكاء الاصطناعي والتعلم الآلي، حيث تم تدريبه على مجموعة بيانات ضخمة ، وذلك بهدف تقديم معلومات طبية يشكل سريع. ومع ذلك، من المهم الإشارة إلى أن التطبيق لا يغني عن استشارة الطبيب المختص او الرجوع الى مصادر هيئة الدواء الموثوقة   ''', unsafe_allow_html=True)




st.link_button("تطبيق التفاعلات الدوائية والتاثيرات الجانبية للادوية", "https://drug-drug-5qohebfrcptarhcj8niwgo.streamlit.app/",use_container_width= True, help="هذا التطبيق يمكّن المستخدمين من الوصول إلى معلومات شاملة حول دواء معين عن طريق تقديم اسمه. يُمكن المستخدمين من إدخال اسم الدواء، حيث سيقوم التطبيق بجلب معلومات مفصلة حول جوانب متنوعة، تشمل ولكن لا تقتصر على الدلالات، والتوجيهات، والتحذيرات، والآثار الجانبية المحتملة، وأي تفاعلات معروفة مع الأدوية الأخرى")

st.link_button("تطبيق التفاعلات الدوائية مع الاطعمة", "https://drug-drug-interaction-hyk3pkub6bayodgp2nnuya.streamlit.app/", use_container_width= True, help=" هذا التطبيق يمكن المستخدمين من الوصول إلى معلومات شاملة حول طعام معين وتفاعلاته المحتملة مع الأدوية عن طريق تقديم اسمه. يُمكن المستخدمين من إدخال اسم الطعام، حيث سيقوم التطبيق بجلب معلومات مفصلة حول جوانب متنوعة، تشمل ولكن لا تقتصر على تفاعلات محتملة مع أدوية معينة ")

st.link_button("تطبيق دليل التغذية لمرضى السكروالضغط وارتفاع نسبة الكوليسترول", "https://dpc-eda-iwjjdpb87qynvv5zjprgqb.streamlit.app/", use_container_width= True, help=" هذا التطبيق يمكن المستخدمين من الوصول إلى معلومات شاملة حول طعام معين وتاثيره على مرضى السكر او ضغط الدم او مرضى الذين يعانون من ارتفاع نسبة الكوليسترول عن تقديم صورة. يُمكن المستخدمين من إدخال صورة الطعام، حيث سيقوم التطبيق بجلب معلومات مفصلة حول تاثيره على الامراض المذكورة مسبقا ")

#st.link_button("Alternative HPLC Columns App ", "https://all-columns-hfhgedeitmrzrhrlujtvoc.streamlit.app/", use_container_width= True, help=" هذا التطبيق يمكن المستخدمين من اختيار البدائل لاعمدة الفصل")

st.link_button("تطبيق التفاعل مع الذكاء الاصطناعي بمهام متعددة", "https://evastauxeasqz3wahcrvmh.streamlit.app/", use_container_width= True, help="  هذا التطبيق يمكن المستخدمين من الاجابة على الاسئلة ")

#st.link_button("Assay Calculations App ", "https://elnegmelnegm-first-app-ydrlh3.streamlit.app/", use_container_width= True, help="This application enables users to calculate the assay. هذا التطبيق يمكن المستخدمين من حساب نسبة المادة ")

#st.link_button("Molar Mass Calculator App ", "https://elnegmelnegm-molar-mass-application-app2-ck9xdr.streamlit.app/", use_container_width= True, help="This application enables users to calculate weight. هذا التطبيق يمكن المستخدمين من حساب الوزن  ")

#st.link_button("Information about used model", "https://storage.googleapis.com/deepmind-media/gemini/gemini_1_report.pdf", type="primary",use_container_width= True)



