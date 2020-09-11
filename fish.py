
'''
   
static int EatFish(int[] A, int[] B)       
 {            
    var n = A.Length;            
    var downstreamStack = new Stack<int>();            
    for (var i = 0; i < A.Length; i++)      
    {                if(B[i] == 1){                   
         // fish is flowing downstream                    
         // store its size                    
         downstreamStack.Push(A[i]);               
          }                else{                    
              if(downstreamStack.Count > 0){ 
                                         // there is a fish that was flowing downstream            
                                                     // eating is done                       
                                                      if(downstreamStack.Peek() < A[i]){      
                                                                                // downstream fish is smaller, should be eaten    
                                                                                                        downstreamStack.Pop();   
                                                                                                                             }     
                                                                                                                                                n--;          
                                                                                                                                                          }          
                                                                                                                                                                }      
                                                                                                                                                                      }           
                                                           return n;        }
 {
             if(B[i] == 1)
            {                   
                 // fish is flowing downstream                    
                 // store its size                    
                 downstreamStack.Push(A[i]);               
            }  
            else
            {
                if(downstreamStack.Count > 0)
                { 
                    if(downstreamStack.Peek() < A[i])
                    {
                        downstreamStack.Pop();
                        
                    }
                    n--;
                }
              }
            }
            return n;
        }
'''