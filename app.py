import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title='Productivity Dashboard', layout='wide')

# Load Data
@st.cache_data
def load_data():
    df_r = pd.read_csv('2 week records (Routines).csv')
    df_e = pd.read_csv('2 week records (Events).csv')
    df_r['Date'] = pd.to_datetime(df_r['Date'])
    df_e['Date'] = pd.to_datetime(df_e['Date'])
    return pd.merge(df_r, df_e, on='Date', how='left')

df_raw = load_data()
df = df_raw.copy()

# Sidebar Navigation
st.sidebar.title("Routine and Efficiency Analysis Dashboard")
st.sidebar.divider()
st.sidebar.subheader("Navigation")
page = st.sidebar.radio("Go to", ["Story Overview", "Key Insights", "Decision", "Ethics and Responsibility"])

# Sidebar Filters
if page == "Key Insights":
    st.sidebar.divider()
    st.sidebar.subheader("Data Filters")

    # Period Filter
    week_options = ['All Weeks', 'Exam Week', 'Non-Exam Week'] + [f'Week {int(w)}' for w in sorted(df_raw['Week_No'].unique())]
    selected_filter = st.sidebar.selectbox("Select Period", week_options)

    if selected_filter == 'Exam Week':
        df = df_raw[df_raw['Exam_Week'] == True]
    elif selected_filter == 'Non-Exam Week':
        df = df_raw[df_raw['Exam_Week'] == False]
    elif selected_filter.startswith('Week'):
        w_num = int(selected_filter.split(' ')[1])
        df = df_raw[df_raw['Week_No'] == w_num]
    else:
        df = df_raw.copy()

    # Activity Filter
    activity_list = ['All Activities'] + sorted(df_raw['Activity'].unique().tolist())
    selected_activity = st.sidebar.selectbox("Select Activity", activity_list)

    if selected_activity != 'All Activities':
        df = df[df['Activity'] == selected_activity]

# Page: Story Overview
if page == "Story Overview":
    st.title("📖 Self Analysis")
    st.markdown("""
    ### Project Context
    * I chose this topic to analyse myself. How I behave? What do I like to spend more time in? Am I efficient in processes? 
    The data is collected starting from May 4th, 2026 to May 24th, 2026. It is exactly three weeks. 
    Within those three weeks I have encountered external factors like electricity cuts and connection problems and I have learnt a lot about my general activity of each day including how much time I spent and how efficient I was doing those activities.  
    * It is important for me because the project can help me realise my own behaviors and activities and how I am affected by external factors. It can give me information on deciding how can I improve in my daily life to be more efficient and become more productive.
    """)
    st.image("https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?auto=format&fit=crop&q=80&w=1000", caption="Data-Driven Growth")

# Page: Key Insights
elif page == "Key Insights":
    st.title("📊 Data Insights & Trends")

    # Metrics calculation (skipping 0h activities)
    df_for_metric = df[df['Hour'] > 0]

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Avg Efficiency", f"{df_for_metric['Efficiency_score'].mean():.2f}" if not df_for_metric.empty else "0.00")
    c2.metric("Avg Activity Hours", f"{df['Hour'].mean():.2f}" if not df.empty else "0.00")
    c3.metric("Total Hours", f"{df['Hour'].sum():.1f}" if not df.empty else "0.0")
    c4.metric("Data Points", len(df))

    st.divider()

    if df.empty:
        st.warning("No data available for the selected filters.")
    else:
        # Section 1: Efficiency Trend
        st.subheader("1. Efficiency Trend Over Time")
        if selected_activity == 'All Activities':
            trend_data = df[df['Hour'] > 0]
        else:
            trend_data = df
        daily_eff = trend_data.groupby('Date')['Efficiency_score'].mean().reset_index()
        fig_line_eff = px.line(daily_eff, x='Date', y='Efficiency_score', markers=True, template='plotly_white', height=400)
        st.plotly_chart(fig_line_eff, use_container_width=True)
        st.markdown("Efficiency trends average around 2.8 overall. Later upward trends indicating that the efficiency increased in Exam week. Especially average study efficiency increased sharply in Exam week. Possibly due to crunchig time to complete tasks to study for exam")

        # Section 2: Activity Hours
        st.subheader("2. Activity Hours Trend")
        activity_trend = df.groupby(['Date', 'Activity'])['Hour'].sum().reset_index()
        fig_line_hours = px.line(activity_trend, x='Date', y='Hour', color='Activity', markers=True, template='plotly_white', height=400)
        st.plotly_chart(fig_line_hours, use_container_width=True)

        # Section 3: Time Allocation
        st.subheader("3. Total Time Allocation")
        activity_data = df.groupby('Activity')['Hour'].sum().reset_index()
        fig_pie = px.pie(activity_data, values='Hour', names='Activity', hole=0.4, height=400)
        st.plotly_chart(fig_pie, use_container_width=True)
        st.markdown("A significant portion of my time is dedicated to Sleep and Screen Time. Screen Time reaching maximum 11 hours in Non-exam week. And average study time increased over 2.5 times in exam week. This indicates I am either a deadline fighter with procrastination problem or really like studying only in exam weeks")

        # Section 4: Correlation
        st.subheader("4. Factor Correlation Heatmap")
        corr_base = df[df['Hour'] > 0].copy()
        if not corr_base.empty:
            corr_df = corr_base.groupby('Date').agg({
                'Efficiency_score': 'mean',
                'Electricity_Cuts': 'first',
                'Connection_Issue': 'first',
                'Exam_Week': 'first'
            }).reset_index()
            corr_df['Electricity_Cuts'] = pd.factorize(corr_df['Electricity_Cuts'])[0]
            corr_df['Connection_Issue'] = pd.factorize(corr_df['Connection_Issue'])[0]
            corr_df['Exam_Week'] = corr_df['Exam_Week'].astype(int)
            matrix = corr_df[['Efficiency_score', 'Electricity_Cuts', 'Connection_Issue', 'Exam_Week']].corr()
            fig_heat = px.imshow(matrix, text_auto=".2f", color_continuous_scale='RdBu_r', height=400)
            st.plotly_chart(fig_heat, use_container_width=True)
        else:
            st.info("Filter settings returned no non-zero activity data for correlation.")

        st.divider()

        # Section 5 & 6: Impact Analysis
        col_a, col_b = st.columns(2)
        with col_a:
            st.subheader("5. Impact of Electricity Cuts")
            elec_impact = df_for_metric.groupby('Electricity_Cuts')['Efficiency_score'].mean().reset_index()
            fig_elec = px.bar(elec_impact, x='Electricity_Cuts', y='Efficiency_score', color='Electricity_Cuts', labels={'Efficiency_score': 'Avg Efficiency'}, template='plotly_white', height=400)
            st.plotly_chart(fig_elec, use_container_width=True)

        with col_b:
            st.subheader("6. Impact of Connection Issues")
            conn_impact = df_for_metric.groupby('Connection_Issue')['Efficiency_score'].mean().reset_index()
            fig_conn = px.bar(conn_impact, x='Connection_Issue', y='Efficiency_score', color='Connection_Issue', labels={'Efficiency_score': 'Avg Efficiency'}, template='plotly_white', height=400)
            st.plotly_chart(fig_conn, use_container_width=True)
        
        st.markdown(" External factors clearly dictate my productivity. 'Severe' disruptions lead to a measurable drop in average task efficiency. Indicating that both connection and electricity are necessary for my overall improvement")

        st.divider()
        st.subheader("📥 Export Data")
        st.write("Download the filtered data used in this view for further analysis.")
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Filtered CSV",
            data=csv,
            file_name='filtered_productivity_data.csv',
            mime='text/csv',
        )

elif page == "Decision":
    st.title("💡 Data-Driven Decisions")
    st.markdown("""
    ### Insights for Future Planning:
    * **Scheduling Study time and other important activities:** To increase efficiency in my routines and be able to face electricity cuts and connection problems.
    * **Adjusting Screen Time:** reducing screen time will be helpful since it take majority of the time of the days. And extra time could be allocated to other activities such as study in non-exam week to avoid last minute preparations.
    """)

elif page == "Ethics and Responsibility":
    st.title("🛡️ Ethics & Responsibility")
    st.subheader("🔒 Privacy Statement")
    st.markdown("""
    * **What data is included?:** Non-sensitive data such as general activity (eg. screen time, sleep) and public data such as electricity cuts.
    * **What is anonymized?:** Information such as my name, exact details on the activity (such as who I socialise with) are excluded. So, there is no identifiable information in the data set.
    """)
    st.divider()
    st.subheader("⚠️ Bias & Limitation Disclosure")
    st.markdown("""
    * **Memory bias:** Some data input(such as electricity problems and hours before May 10th) are from memory. So, the data may slight over or under represent the exact activities happened.
    * **Subjective Scoring:** The data set include efficiency score which is scored subjectively from how I felt during that activity on that day. It is not a standard metric.
    * **Small Dataset:** The dataset is relatively small (only 3 week worth of data), it might not fully describe my activities and events across the year
    """)
    st.divider()
    st.subheader("📊 Visualization Justification")
    st.markdown("""
    * **Line Chart for Avg Efficiency Trend:** As I would like to show trend, I think line chart is the most clear choice since it can show ups and downs clearly.
    * **Line Chart for Hours spend on Activity:** Even though it looks crowded on default, it can show clear trends when filtered. Similar to the previous reason.
    * **Pie Chart for actvities per rweek:** As I would like to show the distribution of activity time in the weeks and the categories are not many, I chose pie chart to represent the data.
    * **Correlation Heat Map for factors and Avg efficienc:** To show the correlation cleary to the audience, heat map is used instead of scatter plot.
    * **Bar Chart for impact on avg efficiency:** To compare the impact of external factors, I chose bar chart since it can show the difference clearly and simple to read.

    * **Risk:** Correlation heat map can be hard to interpret for general audience. It can cause misinterpretation. And since the data are daily trends the sharp spikes can look more exaggerated.
    """)
    st.divider()
    st.subheader("🎯 Responsible Decision")
    st.markdown("""
    * **Limitation on Decision:** Since the data set is relatively small (Time-wise and Variable-wise). There can be more factors that can interfere with my activities. This limit my decision to be set upon conditions that available in the dataset.
    """)
    st.divider()
    st.subheader("🤖 AI usage")
    st.markdown("""
    * Gemini 3 Flash is used in the creation of the dashboard and visualization templates. Insights, EDA and Visualizations are done by human.
    """)
