
public class  Mylist <T> {
    private class node{
        private T value;
        private node next;
    }
    private node head;
    private node tail;

    void add(T val){
        node a = new node();
        a.value=val;
        if(head==null){
            head=a;
            tail=a;
        }
        else {
            tail.next=a;
            tail=a;
        }
    }
    T get(int index){
        T a=null;
        node b=head;
        for(int i=-1;i<index;++i){
            a=b.value;
            b=b.next;
        }

        return a;
    }

    public static void main(String[] args) {
        Mylist<String> a= new Mylist<>();
        a.add("str");
        a.add("str2");
        System.out.println( a.get(0));
    }

}
