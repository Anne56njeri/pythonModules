'''
public class Solution {
public int[] PrisonAfterNDays(int[] cells, int N) {
// new result array
if (N == 0)
{
return cells;
}
var res = new int[8];
res = checksArray(cells);
return PrisonAfterNDays(res, N-1);
}
public int[] checksArray(int[] cells)
{
cells[0] = 0;
for (var i = 1; i < cells.Length - 1; i++)
{
if(cells[i-1] == cells[i+1]){
cells[i] = 1;
}
else{
cells[i] = 0;
}
}
cells[cells.Length - 1] = 0;
return cells;
}
}
'''