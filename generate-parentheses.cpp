/*
Question :- Given n pairs of parentheses, write a function to generate all combinations of well - formed parentheses.

Example 1 :
Input : n = 3
Output : [ "((()))", "(()())", "(())()", "()(())", "()()()" ]

Example 2 :
Input : n = 1
Output : ["()"]

*/

class Solution
{
public:
    void getAllComb(string curState, int OBopen, int OBclosed, int N, vector<string> &ans)
    {

        // Base Case: All Brackets Opened and Closed, Max Brackets used
        if (OBopen == N && OBclosed == N)
        {
            ans.push_back(curState);
        }

        // If '(',')' possible, put it and explore further
        // All answers containing a '(' after the curState will be explored and added in the 'ans' vector
        if (OBopen < N)
        {
            getAllComb(curState + '(', OBopen + 1, OBclosed, N, ans);
        }
        // All answers containing a ')' after the curState will be explored and added in the 'ans' vector
        if (OBclosed < OBopen)
        {
            getAllComb(curState + ')', OBopen, OBclosed + 1, N, ans);
        }
    }

    vector<string> generateParenthesis(int n)
    {
        vector<string> ans;

        // Passing the 'ans' vector as reference, all the answers get stored in this array.
        getAllComb("", 0, 0, n, ans);

        return ans;
    }
};