package Java;
/*
Coding challenge: print out all prime numbers up to n
*/
 
class SieveOfEratosthenes
{
    static void sieveOfEratosthenes(int n)
    {
        // Create a boolean array "prime[0..n]" and initialize
        // all entries it as true. A value in prime[i] will
        // finally be false if i is Not a prime, else true.
        boolean boolPrimes[] = new boolean[n+1];
        for(int i=0;i<=n;i++)
            boolPrimes[i] = true; //run through the entire list and set each index to true
         
        for(int p = 2; p*p <=n; p++)//p*p < n because once we hit p*p then 
        {
            // If boolPrimes[p] is not changed, then it is a prime
            if(boolPrimes[p] == true)
            {
                // Update all multiples of p
                for(int i = p*p; i <= n; i += p)
                boolPrimes[i] = false;
            }
        }
         
        // Print all prime numbers
        for(int i = 2; i <= n; i++)
        {
            if(boolPrimes[i] == true)
                System.out.print(i + " ");
        }
    }
     
    // Driver Program to test above function
    public static void main(String args[])
    {
        int n = 30;
        System.out.print("Following are the prime numbers ");
        System.out.println("smaller than or equal to " + n);
        SieveOfEratosthenes g = new SieveOfEratosthenes();
        g.sieveOfEratosthenes(n);
    }
}
 
// This code has been contributed by Amit Khandelwal.