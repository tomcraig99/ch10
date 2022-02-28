from pickle import TRUE
import PatientClass as pa
import ProcedureClass as pr

def main():
    patient = pa.Patient("1", "Matt Jones", "123 Main st, Waco TX 76706", "254-555-7415", True)
    procOne = pr.Procedure("Physical Exam", "2/15/2022", "Dr. Irvine", 250, "1")
    procTwo = pr.Procedure("MRI", "2/15/2022", "Dr. Hamilton", 1500, "1")
    procThree = pr.Procedure("CT Scan", "2/17/2022", "Dr. Drey", 1200, "2")

    print('*** Patient Bill ***')
    print('Name:', patient.get_patient())
    print("Address:", patient.get_add())
    print("Phone:", patient.get_phoneNum())
    print()

    total=0

    if patient.get_iden() == procOne.get_patient():
        print("Procedure:", procOne.get_proc())
        print("Date:", procOne.get_date())
        print("Practitioner:", procOne.get_practitioner())
        print("Charge: ", "$", format(procOne.get_pay(), "<,.2f"), sep='')
        total+=procOne.get_pay()
        print()

    if patient.get_iden() == procTwo.get_patient():
        print("Procedure:", procTwo.get_proc())
        print("Date:", procTwo.get_date())
        print("Practitioner:", procTwo.get_practitioner())
        print("Charge: ", "$", format(procTwo.get_pay(), "<,.2f"), sep='')
        total+=procTwo.get_pay()
        print()
        
    if patient.get_iden() == procThree.get_patient():
        print("Procedure:", procThree.get_proc())
        print("Date:", procThree.get_date())
        print("Practitioner:", procThree.get_practitioner())
        print("Charge: ", "$", format(procThree.get_pay(), "<,.2f"), sep='')
        total+=procThree.get_pay()
        print()

    if patient.get_veteran():
        total*=.6
        
    print("Total Charges: ","$",format(total, "<,.2f"), sep='')

main()