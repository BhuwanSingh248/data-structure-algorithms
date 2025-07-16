int maxProfit(int* prices, int pricesSize) {
 int buy=prices[0];
 int pmax=0;
 for(int i=1;i<pricesSize;i++)
 {
       if(prices[i]<buy)
       buy=prices[i];
       if(pmax<(prices[i]-buy))
       pmax=prices[i]-buy;
 }   return pmax;
}