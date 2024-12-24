import openai
import streamlit as st

# Set your OpenAI API key
openai.api_key = "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"

# Streamlit page setup
st.set_page_config(page_title="Trợ lý AI báo cáo dữ liệu", layout="wide")

# Helper function to interact with OpenAI API
def generate_openai_response(prompt, model="gpt-4", max_tokens=1500):
    """
    Use OpenAI API to generate a response to a prompt.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "Bạn là một trợ lý thông minh, có khả năng trả lời các câu hỏi liên quan đến một bộ dữ liệu lớn."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"


def process_user_query(query):
    """
    Process the user's query, determine how to fetch relevant data from the dataset,
    and return a response using OpenAI's API.
    """
    # Convert the entire dataset to text format (example dataset overview)
    dataset_text = """
    Dataset Overview
    The dataset records information about pharmaceutical businesses in Vietnam, including pharmacies and drug dealers. It contains 16,424 entries across 11 columns, with each row representing a unique business entity. Below are the dataset's features:

    LOAIHINHHN: Represents the type of business, such as "Nhà thuốc" (pharmacy) or "Đại lý bán thuốc của doanh nghiệp" (drug dealer of enterprises).
    PHAMVIHN: Details the scope of operations, including types of drugs allowed for sale, such as "thuốc hóa dược" (chemical drugs) or "thuốc cổ truyền" (traditional medicine).
    DUONG: Provides the street-level address of the business.
    PHUONG: Represents the ward in which the business is located.
    QUAN: Indicates the district where the business operates, such as "TP. Thủ Đức" or "Quận Bình Thạnh."
    CVXLCCHN: Lists the responsible person for the license, though many entries are missing this information.
    NGCAPCCHN: Indicates the date the business license was issued.
    NOICAPCCHN: Shows the issuing authority for the license, typically "Sở Y tế TP.HCM" (Ho Chi Minh City's Health Department).
    GPP_GDP_GSP: Documents certifications such as GPP (Good Pharmacy Practices) or GDP/GSP.
    NGAYCAPGCN: Records the issuance date of the Certificate of Eligibility.
    NGAYHHGCN: Tracks the expiration date of the certificate.
    Data Trends and Features
    Here are the main patterns and insights derived from the dataset:

    1. Business Types (LOAIHINHHN)
    The dataset is dominated by "Nhà thuốc" (pharmacies), which constitute the majority of records.
    A smaller proportion represents drug dealers ("Đại lý bán thuốc").
    2. Geographical Distribution
    Businesses are spread across various districts, with TP. Thủ Đức and Quận Bình Thạnh having significant concentrations of pharmacies.
    Certain wards (PHUONG) within districts like "Phường Linh Xuân" and "Phường Bình Chiểu" feature prominently in the dataset.
    3. Certification Standards (GPP_GDP_GSP)
    The GPP (Good Pharmacy Practices) standard is the most commonly assigned certification, indicating compliance with high-quality practices.
    Some businesses do not have certifications listed, highlighting potential gaps in compliance or data entry.
    4. Licensing Trends
    The column NGCAPCCHN (license issuance date) shows licenses were issued over a broad range of years, with peaks in activity in recent years.
    A notable number of businesses have missing license issuance dates (NGCAPCCHN) or expired licenses (NGAYHHGCN), indicating potential regulatory issues.
    5. Missing Data
    Columns like CVXLCCHN (responsible person's name), NGAYCAPGCN (issuance date of certificate), and NGAYHHGCN (expiration date) have a significant proportion of missing values.
    Missing data suggests that either the information was not recorded properly or some businesses are non-compliant with reporting standards.
    Insights and Interpretation
    Geographic Concentration:

    Pharmacies are concentrated in urbanized districts, particularly TP. Thủ Đức, likely due to higher population density and demand for healthcare services.
    Regulatory Compliance:

    While many businesses have GPP certifications, the missing data in license issuance and expiration dates raises concerns about incomplete regulatory adherence.
    Businesses without proper certifications or expired licenses may need follow-up for compliance.
    Operational Scope:

    Most businesses operate within the scope of selling chemical drugs, traditional medicine, and herbal products, reflecting diverse pharmaceutical demands in the region.
    Trends Over Time:

    Licensing activity shows peaks in certain years, potentially reflecting changes in regulations or an increase in new pharmacy establishments.
    Recommendations for Further Analysis
    Explore Trends by Year: Analyze the number of licenses issued annually to identify growth or decline in the pharmaceutical sector.
    Identify Non-Compliant Businesses: Focus on entries with missing or expired license data to understand compliance issues.
    Assess Geographic Clusters: Create heatmaps to visualize the concentration of pharmacies by district.
    Certification Gaps: Investigate businesses without GPP certifications to understand whether they meet basic operational standards.

    """

    # Construct the system prompt to guide the assistant
    system_prompt = (
        f"Bạn là một trợ lý thông minh, có khả năng trả lời các câu hỏi liên quan đến một bộ dữ liệu lớn. "
        f"Dữ liệu này bao gồm các thông tin sau: \n{dataset_text}\n\n"
        "Bạn sẽ nhận được câu hỏi từ người dùng về bộ dữ liệu này. Hãy làm rõ các câu hỏi, phân tích dữ liệu và "
        "trả lời câu hỏi một cách chi tiết và chính xác nhất bằng Tiếng Việt. Nếu câu hỏi liên quan đến một phần của bộ dữ liệu, "
        "bạn cần biết cách tra cứu và giải thích các dữ liệu có liên quan.\n\n"
        
        f"Câu hỏi từ người dùng: {query}\n"
        "Trợ lý AI:"
    )
    
    # Combine the system prompt with the user's query
    return generate_openai_response(system_prompt)

# Streamlit UI components
st.title("Trợ lý AI báo cáo dữ liệu")
st.markdown("Hãy hỏi về bộ dữ liệu và nhận được các báo cáo chi tiết bằng Tiếng Việt.")

# User input
user_query = st.text_input("Hãy đặt câu hỏi về bộ dữ liệu:")

# Generate response
if user_query:
    with st.spinner("Đang xử lý câu hỏi của bạn..."):
        response = process_user_query(user_query)
    st.subheader("Phản hồi từ Trợ lý AI")
    st.markdown(response)
