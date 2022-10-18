package org.mds.experimental;

import io.reactivex.Observable;
import lombok.Getter;
import lombok.Setter;
import lombok.experimental.Accessors;
import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.Test;

import java.util.*;


@Slf4j
class VertxApplicationTest {

    private int lengthOfLongestSubstring(String s) {
        if (s == null || s.isEmpty()) return 0;
        int len = s.length();
        int ret = 0;
        int left = 0, right = 1;

        char[] chars = s.toCharArray();
        StringBuilder sb = new StringBuilder();

        while (right < len) {

            int found = Arrays.binarySearch(chars, left, right, chars[right]);
            if (found >= 0) {
                ret = Math.max(ret, (right - left));
                left = found + 1;
            }

            right++;
        }
        return Math.max(ret, (right - left));
    }

    @Test
    public void test() {
        this.lengthOfLongestSubstring("abcabcbb");
    }

    @Test
    public void reverse() {
        StringBuilder sb = new StringBuilder();
        sb.append("12d34");
        char[] chars = "12d34".toCharArray();
        Arrays.sort(chars);
        log.info("" + String.valueOf(chars));
        log.info(sb.reverse().toString());
    }

    @Test
    public void sort() {
        TreeMap<Integer, String> treeMap = new TreeMap<>();

        treeMap.put(5, "a");
        treeMap.put(4, "b");

        treeMap.entrySet().stream().sorted(Map.Entry.comparingByValue())
                .forEach(entry -> {
                    log.info(entry.getKey() + ":" + entry.getValue());
                });

        treeMap.forEach((integer, s) -> {
            log.info(integer + ":" + s);
        });

        Observable.fromPublisher(subscriber -> {
            subscriber.onNext(10);
            subscriber.onComplete();
        }).doOnNext(o -> {
            log.info("" + o);
        }).blockingSubscribe();

        log.info("" + Observable.just(1).blockingFirst());
    }

    /**
     * letters=[['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
     * class Solution:
     * def letterCombinations(self, digits: str) -> List[str]:
     * if len(digits)==0: return []
     * strs=[letters[int(s)-2] for s in digits]
     * result=strs[0]
     * for i in range(1,len(strs)):
     * result=[s1+s2 for s1 in result for s2 in strs[i]]
     * return result
     */

    @Test
    public void testNums() {
        char[][] letters = new char[][]{
                new char[]{'a', 'b', 'c'},
                new char[]{'d', 'e', 'f'},
                new char[]{'g', 'h', 'i'},
                new char[]{'j', 'k', 'l'},
                new char[]{'m', 'n', 'o'},
                new char[]{'p', 'q', 'r', 's'},
                new char[]{'t', 'u', 'v'},
                new char[]{'w', 'x', 'y', 'z'},
        };
        String digitals = "23";

        List<char[]> current = new ArrayList<>();
        for (int i = 0; i < digitals.length(); i++) {
            current.add(letters[Integer.parseInt(String.valueOf(digitals.charAt(i))) - 2]);
        }

        //combine(current,0).forEach(log::info);

        List<String> result = new ArrayList<>();

        dfs(result, "", current, 0);

        result.forEach(log::info);
    }

    private List<String> combine(List<char[]> chars, int index) {
        List<String> result = new ArrayList<>();
        if (index == chars.size() - 1) {
            for (char c : chars.get(index)) {
                result.add(String.valueOf(c));
            }
            return result;
        }
        for (char c : chars.get(index)) {
            for (String s : combine(chars, index + 1)) {
                result.add(c + s);
            }
        }
        return result;
    }

    private void dfs(List<String> result, String current, List<char[]> chars, int index) {
        if (index == chars.size()) {
            result.add(current);
            return;
        }
        for (char c : chars.get(index)) {
            dfs(result, current + c, chars, index + 1);
        }
    }

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ret=new ArrayList<>();

        List<TreeNode> stack=new ArrayList<>();
        stack.add(root);

        while (!stack.isEmpty()){
            int size=stack.size();
            List<Integer> cur=new ArrayList<>();
            for(int i=0;i<size;i++){
                TreeNode node=stack.remove(0);
                if(node.left!=null){
                    stack.add(node.left);
                }
                if(node.right!=null){
                    stack.add(node.right);
                }
                cur.add(node.val);
            }
            ret.add(cur);
        }
        return ret;
    }

    private void backtrace(List<List<Integer>> ret,List<Integer> cur,int[] nums,int n){
        if(nums.length==n){
            return;
        }
        ret.add(cur);
        for(int i=n;i<nums.length;i++){
            cur.add(nums[i]);
            backtrace(ret,cur,nums,n+1);
            cur.remove(cur.size()-1);
        }
    }

    public List<List<Integer>> subsets(int[] nums) {
        if(nums==null || nums.length==0) return new ArrayList<>();
        List<List<Integer>> ret=new ArrayList<>();
        backtrace(ret,new ArrayList<>(),nums,0);
        return ret;
    }

    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> queue=new PriorityQueue<>();

        for(int n: nums){
            if(n<k) {
                queue.add(n);
                continue;
            }
            if(n< queue.peek()){
                continue;
            }
            queue.poll();
            queue.add(n);
        }

        return queue.peek();
    }


    class State{
        private int lRow=0,hRow,lCol=0,hCol;
        public boolean nextLRow(){
            this.lRow++;
            if (this.lRow>this.hRow) return false;
            return true;
        }
        public boolean nextHRow(){
            this.hRow--;
            if (this.lRow>this.hRow) return false;
            return true;
        }
        public boolean nextLCol(){
            this.lCol++;
            if (this.lCol>this.hCol) return false;
            return true;
        }
        public boolean nextHCol(){
            this.hCol--;
            if (this.lCol>this.hCol) return false;
            return true;
        }
    }

    public List<Integer> spiralOrder(int[][] matrix) {
        State state=new State();
        state.hCol=matrix[0].length-1;
        state.hRow=matrix.length-1;
        List<Integer> ret=new ArrayList<>();
        while (fillData(ret,matrix,state));
        return ret;
    }

    private boolean fillData(List<Integer> ret,int[][] matrix,State state){
        for(int i=state.lCol;i<=state.hCol;i++){
            ret.add(matrix[state.lRow][i]);
        }
        if(!state.nextLRow()) return false;

        for(int i=state.lRow;i<=state.hRow;i++){
            ret.add(matrix[i][state.hCol]);
        }
        if(!state.nextHCol()) return false;

        for(int i=state.hCol;i<=state.lCol;i--){
            ret.add(matrix[state.hRow][i]);
        }
        if(!state.nextHRow()) return false;

        for(int i= state.hRow;i<=state.lRow;i--){
            ret.add(matrix[i][state.lCol]);
        }
        if(!state.nextLCol()) return false;
        return true;
    }

}