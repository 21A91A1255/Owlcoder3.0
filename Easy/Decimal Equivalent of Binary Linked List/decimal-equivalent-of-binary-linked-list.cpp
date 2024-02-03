//{ Driver Code Starts
// Program to check if linked list is empty or not
#include<iostream>
using namespace std;
const long long unsigned int MOD = 1000000007;

/* Link list Node */
struct Node
{
    bool data;
    struct Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
    
};


// } Driver Code Ends
/* Below global variable is declared in code for modulo arithmetic
const long long unsigned int MOD = 1000000007; */

/* Link list Node/
struct Node
{
    bool data;   // NOTE data is bool
    Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
    
}; */
#include<math.h>
class Solution
{
    public:
        // Should return decimal equivalent modulo 1000000007 of binary linked list 
        long long int mod=(1000000007);
        long long int power(long long int a,long long int b)
        {
            long long int s=1;
            while(b>0)
            {
                if(b%2!=0)
                {
                    s=(s%mod*a%mod)%mod;
                    s=s%mod;
                }
                a=(a%mod * a%mod)%mod;
                b=b/2;
            }
            return s%mod;
        }
        long long unsigned int decimalValue(Node *head)
        {
           // Your Code Here
           long long unsigned int ans=0;
           long long int n=0;
           Node* current = head; 
            while (current != NULL) {
                n++;
                current = current->next;
            }
           while(head!=NULL)
           {
               n=n-1;
               long long int p=power(2,n);
               //cout<<p;
               ans+=((head->data)*(p%mod))%mod;
               ans=ans%mod;
               head=head->next;
               //n=n-1;
           }
           return ans%mod;
        }
};




//{ Driver Code Starts.

void append(struct Node** head_ref, struct Node **tail_ref, bool new_data)
{

    struct Node* new_node = new Node(new_data);
    
    if (*head_ref == NULL)
       *head_ref = new_node;
    else
       (*tail_ref)->next = new_node;
    *tail_ref = new_node;
}


bool isEmpty(struct Node *head);

/* Driver program to test above function*/
int main()
{
    bool l;
    int i, n, T;

    cin>>T;

    while(T--){
    struct Node *head = NULL,  *tail = NULL;

        cin>>n;
        for(i=1;i<=n;i++)
        {
            cin>>l;
            append(&head, &tail, l);
        }
        Solution obj;
        cout << obj.decimalValue(head) << endl;
    }
    return 0;
}
// } Driver Code Ends