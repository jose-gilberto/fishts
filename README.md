# Fishts

## Abstract

Fishts is a library for transforming images represented in matrix form into a time series-like structure, which can be used by clustering algorithms and other functions. The algorithm allows the customization of parameters such as initial and final angles and the value of each step taken between iterations, which can influence the format of the generated series. The method's output is a numpy array where each position is represented by start + step * i, where start is the starting angle, step is the step used by the method and i is the index of the position of the numpy array.

## Example

<div align='center'>
    <h3>Step 0 - Initial Image</h3>
    <img src='./triangle.png' alt='Initial image of a triangle' />
    <br/>
    <br/>
    <h3>Step 1 - Extracting the descriptor</h3>
    <br/>
    <img src='./example.gif'>
    <br/>
    <br/>
    <h3>Step 2 - Final timeseries-like structure</h3>
    <br/>
    <img src='./triangle_series.png'/>
</div>

## More Examples

## Use

## Installing

## Some Applications

## Some Results