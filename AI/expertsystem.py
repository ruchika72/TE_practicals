knowledge_base = {
    "cold": {"symptoms": {"headache", "runny nose", "sneezing", "sore throat"}, "medicines": [
        "Tylenol", "Panadol", "Nasal spray", "Wear warm clothes"]},
    "influenza": {"symptoms": {"sore throat", "fever", "headache", "chills", "body ache"}, "medicines": [
        "Tamiflu", "Panadol", "Zanamivir", "Take a warm bath and do salt gargling"]},
    "typhoid": {"symptoms": {"headache", "abdominal pain", "poor appetite", "fever"}, "medicines": [
        "Chloramphenicol", "Amoxicillin", "Ciproflaxacin", "Azithromycin", "Complete bed rest and take soft diet"]},
    "chicken pox": {"symptoms": {"rash", "body ache", "fever"}, "medicines": [
        "Varicella vaccine", "Immunoglobulin", "Acetomenaphin", "Acyclovir", "Have oatmeal and stay at home"]},
    "measles": {"symptoms": {"fever", "runny nose", "rash", "conjunctivitis"}, "medicines": [
        "Tylenol", "Aleve", "Advil", "Vitamin A", "Get rest and use more liquid"]},
    "malaria": {"symptoms": {"fever", "sweating", "headache", "nausea", "vomiting", "diarrhea"}, "medicines": [
        "Aralen", "Qualaquin", "Plaquenil", "Mefloquine", "Do not sleep in open air and cover your full skin"]}
}

def calculate_similarity(symptoms, disease_symptoms):
    return len(symptoms.intersection(disease_symptoms))

def find_most_probable_disease(symptoms):
    max_similarity = 0
    probable_disease = None
    for disease, info in knowledge_base.items():
        similarity = calculate_similarity(symptoms, info["symptoms"])
        if similarity > max_similarity:
            max_similarity = similarity
            probable_disease = disease
    return probable_disease

def main():
    print("Medical Diagnosis Expert System")
    print("Enter your symptoms separated by comma:")
    symptoms_input = set(input().split(","))
    probable_disease = find_most_probable_disease(symptoms_input)
    if probable_disease:
        print(f"Based on your symptoms, you most likely have {probable_disease}!")
        print("Symptoms:", ', '.join(symptoms_input))
        print("Please take the following medicines and precautions:")
        for med in knowledge_base[probable_disease]["medicines"]:
            print(med)
    else:
        print("Symptoms not found in the knowledge base!")

if __name__ == "__main__":
    main()
