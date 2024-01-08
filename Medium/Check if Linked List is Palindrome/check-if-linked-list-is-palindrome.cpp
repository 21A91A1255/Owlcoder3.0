//{ Driver Code Starts
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <stack>
using namespace std;
/* Link list Node */
struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
};




// } Driver Code Ends
/*
struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
};
*/

class Solution{
  public:
    //Function to check whether the list is palindrome.
    void print(Node *head){
        Node *temp=head;
        while(temp)
        {
            cout<<temp->data<<" ";
            temp=temp->next;
        }
        cout<<endl;
    }
    struct Node *rev(Node *head)
    {
        
        Node *curr=head,*prev=NULL,*next=NULL;
        while(curr){
            next=curr->next;
            curr->next=prev;
            prev=curr;
            curr=next;
        }
        return prev;
    }
    
    bool isPalindrome(Node *head)
    {
        //Your code here
        
        Node *r=NULL,*temp=head,*tail=NULL;
        while(temp)
        {
            Node *nn=new Node(temp->data);
            if(r==NULL && tail==NULL) {
                r=nn;
                tail=nn;
            }
            else{
                tail->next=nn;
                tail=tail->next;
            }
            temp=temp->next;
        }
        // print(head);
        Node *h=rev(head);
        // print(h);
        while(h)
        {
            if(h->data!=r->data)
            
            {
                return false;
            }
            h=h->next;
            r=r->next;
        }
        return true;
    }
};



//{ Driver Code Starts.
/* Driver program to test above function*/
int main()
{
  int T,i,n,l,firstdata;
    cin>>T;
    while(T--)
    {
        
        struct Node *head = NULL,  *tail = NULL;
        cin>>n;
        // taking first data of LL
        cin>>firstdata;
        head = new Node(firstdata);
        tail = head;
        // taking remaining data of LL
        for(i=1;i<n;i++)
        {
            cin>>l;
            tail->next = new Node(l);
            tail = tail->next;
        }
    Solution obj;
   	cout<<obj.isPalindrome(head)<<endl;
    }
    return 0;
}


// } Driver Code Ends