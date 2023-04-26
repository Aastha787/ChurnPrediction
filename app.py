from flask import Flask, request, render_template
import pickle
import DecisionTree as dt
model=pickle.load(open('decisiontree_model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")
def result():
    return render_template("result.html")
      
@app.route('/table', methods=['GET','POST'])
def table():
    if request.method == "POST":
        age=request.form['age']
        last_login= int(request.form['last_login'])
        avg_time=float(request.form['avg_time'])
        avg_tran=float(request.form['avg_tran'])
        points=float(request.form['points'])
        date=request.form['date']
        time=request.form['time']
        gender=request.form['gender']
        region=request.form['region']
        membership=request.form['membership']
        refer=request.form['refer']
        offer=request.form['offer']
        operation=request.form['operation']
        internet=request.form['internet']
        discount=request.form['discount']
        preference=request.form['preference']
        complain=request.form['complain']
        feedback=request.form['feedback']

        if gender=="M":
            gender_M = 1
            gender_Unknown = 0
        elif gender=="Unknown":
            gender_M= 0
            gender_Unknown=1
        else:
            gender_M=0
            gender_Unknown=0

        #region_category
        if region=='Town':
            region_Town=1
            region_Village=0
        if region=='Village':
            region_Town=0
            region_Village=1
        else:
            region_Town=0
            region_Village=0

        #membership category
        if membership=='Gold Membership':
            membership_Gold=1
            membership_No=0
            membership_Platinum=0
            membership_Silver=0
            membership_Premium=0
        elif membership=='No Membership':
            membership_Gold=0
            membership_No=1
            membership_Platinum=0
            membership_Silver=0
            membership_Premium=0
        elif membership=='Platinum Membership':
            membership_Gold=0
            membership_No=0
            membership_Platinum=1
            membership_Silver=0
            membership_Premium=0
        elif membership=='Silver Membership':
            membership_Gold=0
            membership_No=0
            membership_Platinum=0
            membership_Silver=1
            membership_Premium=0
        elif membership=='Premium Membership':
            membership_Gold=0
            membership_No=0
            membership_Platinum=0
            membership_Silver=0
            membership_Premium=1
        else:
            membership_Gold=0
            membership_No=0
            membership_Platinum=0
            membership_Silver=0
            membership_Premium=0
        
        #joined through
        if refer=='No':
            refer_No=1
            refer_Yes=0
        elif refer=='Yes':
            refer_No=0
            refer_Yes=1
        else:
            refer_Yes=0
            refer_No=0
        
        #preffered_offer
        if offer=='Gift Vouchers/Coupons':
           offer_Gift_VouchersCoupons =1
           offer_Without_Offers=0
        if offer=='Without Offers':
           offer_Gift_VouchersCoupons =0
           offer_Without_Offers=1
        else:
           offer_Gift_VouchersCoupons =0
           offer_Without_Offers=0
        
        #medium_of operations
        if operation=='Desktop':
           operation_Desktop =0
           operation_Both=1
           operation_Smartphone=0
        elif operation=='Both':
           operation_Desktop =0
           operation_Both=1
           operation_Smartphone=0
        elif operation=='Smartphone':
           operation_Desktop =0
           operation_Both=1
           operation_Smartphone=0
        else:
           operation_Desktop =0
           operation_Both=0
           operation_Smartphone=0
         
         #internet options
        if internet=='Mobile_Data':
           internet_Mobile_Data =1
           internet_Wi_Fi=0
        if internet=='Wi-Fi':
           internet_Mobile_Data =0
           internet_Wi_Fi=1
        else:
           internet_Mobile_Data =0
           internet_Wi_Fi=0

        #used_special_discount
        if discount=='Yes':
            discount_Yes =1
        else:
            discount_Yes =0

        #offer_application_preference
        if preference=='Yes':
            preference_Yes=1
        else:
            preference_Yes=0

        #past_complains
        if complain=='Yes':
            complain_Yes=1
        else:
            complain_Yes=0

        #feedback
        if feedback=='Poor Customer Service':
            feedback_Poor_Customer_Service=1
            feedback_Poor_Product_Quality=0
            feedback_Poor_Website=0
            feedback_Products_always_in_Stock=0
            feedback_Quality_Customer_Care=0
            feedback_Reasonable_Price=0
            feedback_Too_many_ads=0
            feedback_User_Friendly_Website=0
        elif feedback=='Poor Product Quality':
            feedback_Poor_Customer_Service=0
            feedback_Poor_Product_Quality=1
            feedback_Poor_Website=0
            feedback_Products_always_in_Stock=0
            feedback_Quality_Customer_Care=0
            feedback_Reasonable_Price=0
            feedback_Too_many_ads=0
            feedback_User_Friendly_Website=0
        elif feedback=='Poor Website':
            feedback_Poor_Customer_Service=0
            feedback_Poor_Product_Quality=0
            feedback_Poor_Website=1
            feedback_Products_always_in_Stock=0
            feedback_Quality_Customer_Care=0
            feedback_Reasonable_Price=0
            feedback_Too_many_ads=0
            feedback_User_Friendly_Website=0
        elif feedback=='Products always in stock':
            feedback_Poor_Customer_Service=0
            feedback_Poor_Product_Quality=0
            feedback_Poor_Website=0
            feedback_Products_always_in_Stock=1
            feedback_Quality_Customer_Care=0
            feedback_Reasonable_Price=0
            feedback_Too_many_ads=0
            feedback_User_Friendly_Website=0
        elif feedback=='Quality Customer Care':
            feedback_Poor_Customer_Service=0
            feedback_Poor_Product_Quality=0
            feedback_Poor_Website=0
            feedback_Products_always_in_Stock=0
            feedback_Quality_Customer_Care=1
            feedback_Reasonable_Price=0
            feedback_Too_many_ads=0
            feedback_User_Friendly_Website=0
        elif feedback=='Reasonable Price':
            feedback_Poor_Customer_Service=0
            feedback_Poor_Product_Quality=0
            feedback_Poor_Website=0
            feedback_Products_always_in_Stock=0
            feedback_Quality_Customer_Care=0
            feedback_Reasonable_Price=1
            feedback_Too_many_ads=0
            feedback_User_Friendly_Website=0
        elif feedback=='Too many ads':
            feedback_Poor_Customer_Service=0
            feedback_Poor_Product_Quality=0
            feedback_Poor_Website=0
            feedback_Products_always_in_Stock=0
            feedback_Quality_Customer_Care=0
            feedback_Reasonable_Price=0
            feedback_Too_many_ads=1
            feedback_User_Friendly_Website=0
        elif feedback=='User Friendly Website':
            feedback_Poor_Customer_Service=0
            feedback_Poor_Product_Quality=0
            feedback_Poor_Website=0
            feedback_Products_always_in_Stock=0
            feedback_Quality_Customer_Care=0
            feedback_Reasonable_Price=0
            feedback_Too_many_ads=0
            feedback_User_Friendly_Website=1
        else:
            feedback_Poor_Customer_Service=0
            feedback_Poor_Product_Quality=0
            feedback_Poor_Website=0
            feedback_Products_always_in_Stock=0
            feedback_Quality_Customer_Care=0
            feedback_Reasonable_Price=0
            feedback_Too_many_ads=0
            feedback_User_Friendly_Website=0

        date2 = date.split('-')
        joining_day=int(date2[0])
        joining_month=int(date2[1])
        joining_year=int(date2[2])

        time = request.form['time']

        time2 = time.split(':')
        if len(time2) >= 3:
            last_visit_time_seconds = int(time2[2])
        else:
            last_visit_time_seconds = 0 

        last_visit_time_hour = int(time2[0])
        last_visit_time_minutes = int(time2[1])

        data= {'age':[age], 'days_since_last_login':[last_login], 'avg_time_spent':[avg_time],
       'avg_transaction_value':[avg_tran], 'points_in_wallet':[points],
       'joining_day':[joining_day], 'joining_month':[joining_month], 'joining_year':[joining_year], 'last_visit_time_hour':[last_visit_time_hour],
       'last_visit_time_minutes':[last_visit_time_minutes], 'last_visit_time_seconds':[last_visit_time_seconds], 'gender_M:':[gender_M],
       'gender_Unknown':[gender_Unknown], 'region_category_Town':[region_Town], 'region_category_Village':[region_Village],
       'membership_category_Gold Membership':[membership_Gold],
       'membership_category_No Membership':[membership_No],
       'membership_category_Platinum Membership':[membership_Platinum],
       'membership_category_Premium Membership':[membership_Premium],
       'membership_category_Silver Membership':[membership_Silver], 'joined_through_referral_No':[refer_No],
       'joined_through_referral_Yes':[refer_Yes],
       'preferred_offer_types_Gift Vouchers/Coupons':[offer_Gift_VouchersCoupons],
       'preferred_offer_types_Without Offers':[offer_Without_Offers], 'medium_of_operation_Both':[operation_Both],
       'medium_of_operation_Desktop':[operation_Desktop], 'medium_of_operation_Smartphone':[operation_Smartphone],
       'internet_option_Mobile_Data':[internet_Mobile_Data], 'internet_option_Wi-Fi':[internet_Wi_Fi],
       'used_special_discount_Yes':[discount_Yes], 'offer_application_preference_Yes':[preference_Yes],
       'past_complaint_Yes':[complain_Yes], 'feedback_Poor Customer Service':[feedback_Poor_Customer_Service],
       'feedback_Poor Product Quality':[feedback_Poor_Product_Quality], 'feedback_Poor Website':[feedback_Poor_Website],
       'feedback_Products always in Stock':[feedback_Products_always_in_Stock], 'feedback_Quality Customer Care':[feedback_Quality_Customer_Care],
       'feedback_Reasonable Price':[feedback_Reasonable_Price], 'feedback_Too many ads':[feedback_Too_many_ads],
       'feedback_User Friendly Website':[feedback_User_Friendly_Website]}
        
        import pandas as pd
        df= pd.DataFrame.from_dict(data)       

        table = model.predict(df.values)

        return render_template("result.html", table_text="Churn Score is {}".format(table))

    else:
         return render_template("table.html")
@app.route('/metrics')
def metrics():
    return render_template("metrics.html")
   
@app.route('/policy')
def policy():
    return render_template("policy.html")


if __name__ == "__main__":
    app.run(debug=True)