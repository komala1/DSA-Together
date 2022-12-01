pair<long long, long long> getMinMax(long long a[], int n) {
    int min1 = a[0];
    int max1 = a[0];
    for(int i=0;i<n;i++)
    {
        if(a[i]>max1)
        {
            max1 = a[i];
        }
        if(a[i+1]<min1)
        {
            min1 = a[i+1];
        }
    }
    return {min1,max1};
}
