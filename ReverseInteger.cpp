class Solution {
public:
    int reverse(int x) {
    long long int sum = 0;
    int min = INT_MIN;
    int max = INT_MAX;
while(x!=0)
{
    sum=sum*10+(x%10);
    x=x/10;
}
    return(sum<min || sum>max)?0:sum;    
    }
};
    
