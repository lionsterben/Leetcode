import java.util.Arrays;
import java.util.HashSet;
class Solution {
    public int coinChange(int[] coins, int amount) {
        if (amount == 0){return 0;}
        Set tocheck = new HashSet();
        tocheck.add(amount);
        int count = 0;
        Arrays.sort(coins);
        while (! tocheck.isEmpty()){
            count += 1;
            Set temp = new HashSet();
            for (Iterator it = tocheck.iterator();it.hasNext();){
                int x = (int)it.next();
                for (int j=0; j<coins.length; j++){
                    int coin = coins[j];
                    if (x == coin){
                        return count;
                    }
                    if (x > coin){
                        temp.add(x-coin);
                    }
                    if (x < coin){
                        break;
                    }
                }
            }
                tocheck = temp;
        
        }
        return -1;
            
    }
}

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0 for _ in range(amount+1)]
        dp[0] = 0
        for money in range(1, amount+1):
            res = amount + 1
            for coin in coins:
                if money >= coin and dp[money-coin] != amount+1:
                    res = min(dp[money-coin]+1, res)
            dp[money] = res
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]

class Solution {
    public int coinChange(int[] coins, int amount) {
    if (amount < 1) return 0;
    int[] dp = new int[amount + 1]; 
    Arrays.fill(dp, Integer.MAX_VALUE);
    dp[0] = 0;
    for (int coin : coins) {
        for (int i = coin; i <= amount; i++) {
            if (dp[i - coin] != Integer.MAX_VALUE) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
    }
    return dp[amount] == Integer.MAX_VALUE ? -1 : dp[amount];
}
}

class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount+1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        for (int money=1; money <= amount; money++){
            for (int i=0; i<coins.length;i++){
                int coin = coins[i];
                if (money >= coin && dp[money-coin] != Integer.MAX_VALUE){
                    dp[money] = Math.min(dp[money-coin]+1, dp[money]);
                }
            }
        }
        // System.out.println(dp[2]);
        return dp[amount] == Integer.MAX_VALUE ? -1 : dp[amount];
    }
}