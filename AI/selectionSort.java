package com.ruchika;

import java.util.Arrays;

public class selectionSort {
    public static void main(String[] args) {
        int[] arr = {4,5, 1,2,3};
        ssort(arr);
        System.out.println(Arrays.toString(arr));


    }

    static void ssort(int[] arr){

        for(int i = 0 ; i < arr.length ; i++ ){
            int max = maxElement(arr , 0 , arr.length- i-1);
            swap(arr, max , arr.length - i -1);

        }

    }

    static int maxElement(int[] arr , int start , int end ){
        int max = start ;
        for(int i = start ; i <= end ; i++) {
            if (arr[max] < arr[i]) {
                max = i ;
            }
        }
        return max;

    }

    static void swap(int[] arr , int index1 , int index2){

        int temp = arr[index1] ;
        arr[index1] = arr[index2];
        arr[index2] = temp;

    }
}
