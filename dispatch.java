class Phone{
    public void greet(){
        System.out.println("good morning");
    }
    public void on(){
        System.out.println("turning on phone");
    }
}


class smartphone extends Phone{
    public void swagat(){
        System.out.println("good morning");
    }
    public void on(){
        System.out.println("turning on smartphone");
    }
}

public class dispatch {
    public static void main(String[] args) {
        // Phone obj = new Phone();   // ALLOWED 
        // smartphone smobj = new smartphone(); // allowed
        // obj.name();
        Phone obj = new smartphone();  // yes it is allowed
        // smartphone obj2 = new Phone(); // not allowed
        obj.greet();
        obj.on();
        
    }
}
