{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7ada61c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pickle\n",
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "82c81a78",
   "metadata": {},
   "outputs": [],
   "source": [
    "primaryColor = \"#438E8E\"\n",
    "backgroundColor = \"#0E1117\"\n",
    "secondaryBackgroundColor = \"#337367\"\n",
    "textColor = \"#FAFAFA\"\n",
    "font = \"sans serif\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1b76137b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# loading the saved model\n",
    "loaded_model = pickle.load(open(r'C:/Users/D. PURNA/Desktop/New folder/model_saved', 'rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "cac593ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "CURRENT_THEME = \"DARK\"\n",
    "IS_DARK_THEME = True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d96ffcca",
   "metadata": {},
   "outputs": [],
   "source": [
    "# creating a function for Prediction\n",
    "\n",
    "def Employee_performance_prediction(input_data):\n",
    "    \n",
    "\n",
    "    # changing the input_data to numpy array\n",
    "    input_data_as_numpy_array = np.asarray(input_data)\n",
    "\n",
    "    # reshape the array as we are predicting for one instance\n",
    "    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)\n",
    "\n",
    "    prediction = loaded_model.predict(input_data_reshaped)\n",
    "    print(prediction)\n",
    "\n",
    "    if (prediction== 1):\n",
    "      return 'The performance of an employee is EXCELLENT'\n",
    "    elif (prediction== 2):\n",
    "      return 'The performance of an employee is GOOD'\n",
    "    elif (prediction== 3):\n",
    "      return 'The performance of an employee is LOW'\n",
    "    else:\n",
    "      return 'The performance of an employee is OUTSTANDING'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c19eb549",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-11-08 11:21:04.597 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\D. PURNA\\anaconda3\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2022-11-08 11:21:04.602 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "def main():\n",
    "    primaryColor = \"#438E8E\"\n",
    "    backgroundColor = \"#0E1117\"\n",
    "    secondaryBackgroundColor = \"#337367\"\n",
    "    textColor = \"#FAFAFA\"\n",
    "    font = \"sans serif\"\n",
    "    CURRENT_THEME = \"DARK\"\n",
    "    IS_DARK_THEME = True\n",
    "\n",
    "    # giving a title\n",
    "    st.header(\" Employee Performance prediction Web App\")\n",
    "    st.subheader(\"This app evaluates the Performance of an Employee\")\n",
    "    #Placing a image file\n",
    "    #from PIL import Image\n",
    "    st.image(\"https://fellow.app/wp-content/uploads/2021/04/59-1536x864.jpg\")\n",
    "    st.write(\"\"\"Any business's success depends on its employees. Businesses that realize this are concerned about employee output and productivity. Productivity has a compounding effect at the different levels in the workplace, meaning that high productivity at a lower level of organization paves way for higher productivity at the higher levels of the organization. Hence, analysis of performance of employees in any organization is the need of the hour. Performance of an employee cannot be attributed to any fixed quality. Different people have different skill sets and different behavioral characteristics. Thus, performance analysis requires data to be gathered from all walks of life.\"\"\")\n",
    "    st.subheader(\"\"\"Let us evaluate the performance of employees in an organization on the basis of various factors\"\"\")\n",
    "    st.sidebar.image(\"https://www.centranum.com/wp-content/uploads/2016/08/performance-ratings.png\")\n",
    "    st.sidebar.header(\"Specify Input Metrics Here\")   \n",
    "    \n",
    "    Age = st.sidebar.slider(\"Age of Employee\", 20,60)\n",
    "   \n",
    "    years_of_experience = st.sidebar.slider(\"Experience of employee\", 0, 40)\n",
    "    \n",
    "   \n",
    "    Gender = st.sidebar.radio(\"Gender\",[\"Male\",\"Female\"])\n",
    "    if Gender =='Male': \n",
    "     Gender =1\n",
    "    else:\n",
    "     Gender=0\n",
    "    \n",
    "    \n",
    "    Marital_Status = st.sidebar.radio(\"Marital status\",[\"Single\",\"Married\",\"Divorced\"])\n",
    "    if Marital_Status =='Single': \n",
    "     Marital_Status =2\n",
    "    elif Marital_Status =='Married': \n",
    "     Marital_Status =1\n",
    "    else:Marital_Status=0\n",
    "    \n",
    "    \n",
    "    Department = st.sidebar.selectbox(\"Department\",[\"Digital_Marketing\",\"Finance\",\"Human_Resource\",\"Management\",\"Research_and_Development\",\"Quality_assurance\",\"Computers_and_information_technology\",\"Customer_service\"])\n",
    "    if Department =='Digital_Marketing': \n",
    "        Department =2\n",
    "    elif Department =='Finance': \n",
    "        Department =3\n",
    "    elif Department =='Human_Resource': \n",
    "        Department =4\n",
    "    elif Department =='Management': \n",
    "        Department =5\n",
    "    elif Department =='Research_and_Development': \n",
    "        Department =7\n",
    "    elif Department =='Quality_assurance': \n",
    "        Department =6\n",
    "    elif Department =='Computers_and_information_technology': \n",
    "        Department =0\n",
    "    else:\n",
    "        Department=1\n",
    "    \n",
    "    \n",
    "    Job_role = st.sidebar.selectbox(\"Job role\",['Accoutant','Actuary','Administrative_Services_Manager','Budget_analyst','Business_Development',\n",
    "                                                'Compensation_and_Benefits','Computer_Information_Systems_Manager','Content_marketer','Customer_service_manager',\n",
    "                                                'Customer_service_representative','Customer_service_supervisor','Customer_support_engineer','Data_scientist','Database_administrator',\n",
    "                                                'Digital_marketing_coordinator','Fianancial_manager','Finance_analyst','Financial_adviser','Financial_manager','Full_stack_developer',\n",
    "                                                'HR_manager','Loan_officer','Marketing_analyst','Marketing_assistant','Marketing_executive','Marketing_Manager','Network_administrator',\n",
    "                                                'Product_marketing','Quality_analyst','Quality_assurance_manager','Quality_assurance_tester','Quality_auditor','Quality_control_supervisor',\n",
    "                                                'Quality_coordinator','Quality_engineer','Quality_technician','R&D_analyst','R&D_engineer','R&D_Manager','R&D_scientist','Recruiting_and_Staffing',\n",
    "                                                'Safety_and_Compliance','Sales_manager','Senior_software_engineer','Social_media_marketing_coordinator','Software_application_packager',\n",
    "                                                'Strategic_Planner','Systems_analyst','Talent_Management','Training_and_Development'])\n",
    "  \n",
    "    if Job_role =='R&D_engineer': \n",
    "        Job_role =37\n",
    "    elif Job_role =='Software_application_packager': \n",
    "        Job_role =45\n",
    "    elif Job_role =='Training_and_Development': \n",
    "        Job_role =49\n",
    "    elif Job_role =='Talent_Management': \n",
    "        Job_role =48\n",
    "    elif Job_role =='Business_Development': \n",
    "        Job_role =4\n",
    "    elif Job_role =='R&D_analyst': \n",
    "        Job_role =36\n",
    "    elif Job_role =='Financial_manager': \n",
    "        Job_role =18\n",
    "    elif Job_role =='Network_administrator':\n",
    "        Job_role =26\n",
    "    elif Job_role =='Product_marketing': \n",
    "        Job_role =27\n",
    "    elif Job_role =='HR_manager': \n",
    "        Job_role =20\n",
    "    elif Job_role =='Database_administrator': \n",
    "        Job_role =13\n",
    "    elif Job_role =='Loan_officer': \n",
    "        Job_role =21\n",
    "    elif Job_role =='Budget_analyst': \n",
    "        Job_role =3\n",
    "    elif Job_role =='Administrative_Services_Manager': \n",
    "        Job_role =2\n",
    "    elif Job_role =='R&D_scientist': \n",
    "        Job_role =39\n",
    "    elif Job_role =='Data_scientist': \n",
    "        Job_role =12\n",
    "    elif Job_role =='Quality_auditor': \n",
    "        Job_role =31\n",
    "    elif Job_role =='Marketing_Manager': \n",
    "        Job_role =25\n",
    "    elif Job_role =='Customer_service_manager': \n",
    "        Job_role =8\n",
    "    elif Job_role =='Safety_and_Compliance': \n",
    "        Job_role =41\n",
    "    elif Job_role =='Marketing_assistant': \n",
    "        Job_role =23\n",
    "    elif Job_role =='Customer_service_representative': \n",
    "        Job_role =9\n",
    "    elif Job_role =='Systems_analyst': \n",
    "        Job_role =47\n",
    "    elif Job_role =='Customer_support_engineer': \n",
    "        Job_role =11\n",
    "    elif Job_role =='R&D_Manager': \n",
    "        Job_role =38\n",
    "    elif Job_role =='Compensation_and_Benefits': \n",
    "        Job_role =5\n",
    "    elif Job_role =='Full_stack_developer':\n",
    "        Job_role =19\n",
    "    elif Job_role =='Actuary':\n",
    "        Job_role =1\n",
    "    elif Job_role =='Quality_analyst': \n",
    "        Job_role =28\n",
    "    elif Job_role =='Marketing_analyst': \n",
    "        Job_role =22\n",
    "    elif Job_role =='Strategic_Planner': \n",
    "        Job_role =46\n",
    "    elif Job_role =='Quality_control_supervisor': \n",
    "        Job_role =32\n",
    "    elif Job_role =='Quality_engineer': \n",
    "        Job_role =34\n",
    "    elif Job_role =='Digital_marketing_coordinator': \n",
    "        Job_role =14\n",
    "    elif Job_role =='Accoutant ': \n",
    "        Job_role =0\n",
    "    elif Job_role =='Finance_analyst ': \n",
    "        Job_role =16\n",
    "    elif Job_role =='Sales_manager': \n",
    "        Job_role = 42\n",
    "    elif Job_role =='Computer_Information_Systems_Manager': \n",
    "        Job_role = 6\n",
    "    elif Job_role =='Recruiting_and_Staffing': \n",
    "        Job_role = 40\n",
    "    elif Job_role =='Fianancial_manager': \n",
    "        Job_role = 15\n",
    "    elif Job_role =='Content_marketer': \n",
    "        Job_role = 7\n",
    "    elif Job_role =='Customer_service_supervisor': \n",
    "        Job_role = 10\n",
    "    elif Job_role =='Quality_technician': \n",
    "        Job_role = 35\n",
    "    elif Job_role =='Quality_assurance_manager': \n",
    "        Job_role = 29\n",
    "    elif Job_role =='Quality_coordinator': \n",
    "        Job_role = 33\n",
    "    elif Job_role =='Senior_software_engineer': \n",
    "        Job_role = 43\n",
    "    elif Job_role =='Social_media_marketing_coordinator': \n",
    "        Job_role =44\n",
    "    elif Job_role =='Marketing_executive ': \n",
    "        Job_role =24\n",
    "    elif Job_role =='Financial_adviser': \n",
    "        Job_role =17\n",
    "    else : \n",
    "        Job_role =30\n",
    "    \n",
    "    \n",
    "    Education_level = st.sidebar.selectbox(\"Education Level\",['1','2','3','4','5'])\n",
    "    st.sidebar.caption(\"1:Below PUC, 2:PUC, 3:Bachelor, 4:Master, 5:Doctor\")\n",
    "\n",
    "\n",
    "    Work_Environment_Satisfaction_Level = st.sidebar.selectbox(\"Work Environment Satisfaction Level\",['1','2','3','4'])\n",
    "    st.sidebar.caption(\"1:low, 2:Medium, 3:High, 4:Very High\")\n",
    "\n",
    "\n",
    "    JobInvolvement = st.sidebar.selectbox(\"Job Involvement\",['1','2','3','4'])\n",
    "    st.sidebar.caption(\"1:low, 2:Medium, 3:High, 4:Very High\")\n",
    "\n",
    "    \n",
    "    JobLevel = st.sidebar.selectbox(\"Job level\",['1','2','3','4','5'])\n",
    "\n",
    "    \n",
    "    JobSatisfaction = st.sidebar.selectbox(\"Job Satisfaction\",['1','2','3','4'])\n",
    "    st.sidebar.caption(\"1:low, 2:Medium, 3:High, 4:Very High\")\n",
    "\n",
    "\n",
    "    Annual_Income_in_lacs  = st.sidebar.slider(\"Annual Income in lacks\",1,30)\n",
    "\n",
    "\n",
    "    RelationshipSatisfaction = st.sidebar.selectbox(\"Relationship Satisfaction\",['1','2','3','4'])\n",
    "    st.sidebar.caption(\"1:low, 2:Medium, 3:High, 4:Very High\")\n",
    "\n",
    "\n",
    "    Working_hrs_per_day = st.sidebar.slider(\"Working hours per day\",6,20)\n",
    "    \n",
    "    Training_Time_in_months = st.sidebar.slider(\"Training Time in months\",1,12)\n",
    "\n",
    "\n",
    "    Work_Life_Balance = st.sidebar.selectbox(\"Work Life Balance\",['1','2','3','4'])\n",
    "    st.sidebar.caption(\"1:Bad, 2:Good, 3:Better, 4:Best\")\n",
    "\n",
    "\n",
    "    Behaviourial_Competence = st.sidebar.selectbox(\"Behaviourial Competence\",['0','1','2','3','4','5'])\n",
    "    st.sidebar.caption(\"0:In-adequate, 1:poor, 2:Satisfactory, 3:good, 4:Very good, 5:Excellent\")\n",
    "\n",
    "\n",
    "    On_Time_Delivery = st.sidebar.selectbox(\"On Time Delivery\",['1','2','3','4','5'])\n",
    "    st.sidebar.caption(\"1:poor, 2:fair, 3:satistfactory, 4:good, 5:Excellent\")\n",
    "\n",
    "\n",
    "    Ticket_Solving_Management = st.sidebar.selectbox(\"Ticket Solving Management\",['1','2','3','4','5'])\n",
    "    st.sidebar.caption(\"1:poor, 2:fair, 3:satistfactory, 4:good, 5:Excellent\")\n",
    "    \n",
    "    \n",
    "    Project_Completion = st.sidebar.slider(\"Projects completed till date\",min_value=0)\n",
    "\n",
    "\n",
    "    Working_Status = st.sidebar.radio(\"Working Status\",[\"WFH\",\"WFO\"])\n",
    "    st.sidebar.caption(\"WFH : Work From Home, WFO : Work From Office \")\n",
    "    if Working_Status =='WFO': \n",
    "     Working_Status =1\n",
    "    else:\n",
    "     Working_Status=0\n",
    "     \n",
    "    \n",
    "    Psycho_social_indicators = st.sidebar.selectbox(\"Psycho social indicators\",['1','2','3','4','5'])\n",
    "    st.sidebar.caption(\"0:In-adequate, 1:poor, 2:Satisfactory, 3:good, 4:Very good, 5:Excellent\")\n",
    "\n",
    "\n",
    "    Feedback = st.sidebar.selectbox(\"Feedback\",['1','2','3','4','5','6'])\n",
    "    st.sidebar.caption(\"1:poor, 2:Not_bad, 3:Satisfactory, 4:Good, 5:Very_good, 6:Outstanding\")\n",
    "\n",
    "\n",
    "    Over_time  = st.sidebar.radio(\"Working Overtime\",['0','1'])\n",
    "    st.sidebar.caption(\"0:No, 1:Yes\")\n",
    "\n",
    "   \n",
    "    Percentage_of_Attendence  = st.sidebar.slider(\"Percentage of Attendence\",0,100)\n",
    "\n",
    "\n",
    "    Effected_with_corona  = st.sidebar.radio(\"Effected with corona\",['0','1'])\n",
    "    st.sidebar.caption(\"0:No, 1:Yes\")\n",
    "\n",
    "   \n",
    "    Percent_salary_hike  = st.sidebar.slider(\"Percentage of salary hike\",0,100)\n",
    "\n",
    "\n",
    "    Net_connectivity  = st.sidebar.radio(\"Have a good Network connectivity \",['0','1'])\n",
    "    st.sidebar.caption(\"0:No, 1:Yes\")\n",
    "\n",
    "    \n",
    "# code for Prediction\n",
    "    Performance_Rating = ''\n",
    "    \n",
    "    # creating a button for Prediction\n",
    "    \n",
    "    if st.button('PREDICT THE PERFORMANCE OF EMPLOYEE'):\n",
    "        Performance_Rating = Employee_performance_prediction([ Age, years_of_experience, Gender, Marital_Status, Department,Job_role, Education_level, \n",
    "                                                              Work_Environment_Satisfaction_Level,JobInvolvement, JobLevel, JobSatisfaction,Annual_Income_in_lacs, \n",
    "                                                              RelationshipSatisfaction,Working_hrs_per_day, Training_Time_in_months, Work_Life_Balance,\n",
    "                                                              Behaviourial_Competence,On_Time_Delivery,Ticket_Solving_Management, Project_Completion, Working_Status,\n",
    "                                                              Psycho_social_indicators, Feedback, Over_time,Percentage_of_Attendence, Effected_with_corona,Percent_salary_hike, \n",
    "                                                              Net_connectivity])\n",
    "        \n",
    "        \n",
    "    st.success(Performance_Rating)\n",
    "    \n",
    "if __name__ == '__main__':\n",
    "\tmain()\n",
    "        "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
