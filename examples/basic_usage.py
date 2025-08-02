#!/usr/bin/env python3
"""
Basic usage examples for py-stats package.

This script demonstrates how to use the various statistical functions
provided by the py-stats package.
"""

import py_stats as ps

def main():
    """Main function demonstrating py-stats usage."""
    
    print("=" * 60)
    print("py-stats: Comprehensive Statistics Package")
    print("=" * 60)
    
    # Sample datasets
    data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    data2 = [10, 20, 30, 40, 50]
    data3 = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Multivariate data
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]
    
    print("\n1. UNIVARIATE STATISTICS")
    print("-" * 30)
    
    print("\n1.1 MEANS")
    print(f"Arithmetic mean of {data1}: {ps.arithmetic_mean(data1):.2f}")
    print(f"Harmonic mean of {data2}: {ps.harmonic_mean(data2):.2f}")
    print(f"Geometric mean of {data2}: {ps.geometric_mean(data2):.2f}")
    print(f"Quadratic mean of {data1}: {ps.quadratic_mean(data1):.2f}")
    
    print("\n1.2 CENTRAL TENDENCY")
    print(f"Median of {data1}: {ps.median(data1):.2f}")
    print(f"Mode of {data3}: {ps.mode(data3)}")
    print(f"Midrange of {data1}: {ps.midrange(data1):.2f}")
    print(f"Trimean of {data1}: {ps.trimean(data1):.2f}")
    
    print("\n1.3 QUANTILES")
    q1, q2, q3 = ps.quartiles(data1)
    print(f"Quartiles of {data1}: Q1={q1:.2f}, Q2={q2:.2f}, Q3={q3:.2f}")
    
    lower_hinge, upper_hinge = ps.hinges(data1)
    print(f"Hinges of {data1}: Lower={lower_hinge:.2f}, Upper={upper_hinge:.2f}")
    
    print(f"25th percentile of {data1}: {ps.quantile(data1, 0.25):.2f}")
    print(f"75th percentile of {data1}: {ps.quantile(data1, 0.75):.2f}")
    
    print("\n1.4 DISPERSION")
    print(f"Sample variance of {data1}: {ps.variance(data1):.2f}")
    print(f"Population variance of {data1}: {ps.variance(data1, population=True):.2f}")
    print(f"Sample standard deviation of {data1}: {ps.standard_deviation(data1):.2f}")
    print(f"Population standard deviation of {data1}: {ps.standard_deviation(data1, population=True):.2f}")
    print(f"Average deviation of {data1}: {ps.average_deviation(data1):.2f}")
    print(f"Median absolute deviation of {data1}: {ps.median_absolute_deviation(data1):.2f}")
    
    print("\n1.5 SHAPE")
    print(f"Skewness of {data1}: {ps.skewness(data1):.4f}")
    print(f"Kurtosis of {data1}: {ps.kurtosis(data1):.4f}")
    
    # Test with skewed data
    skewed_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]
    print(f"Skewness of {skewed_data}: {ps.skewness(skewed_data):.4f}")
    print(f"Kurtosis of {skewed_data}: {ps.kurtosis(skewed_data):.4f}")
    
    print("\n1.6 SPECIALIZED FUNCTIONS")
    angles = [0, 90, 180, 270]
    print(f"Angular mean of {angles} degrees: {ps.angular_mean(angles):.2f}")
    
    print(f"Running average of {data1} (window=3): {ps.running_average(data1, 3)}")
    
    weights = [1, 2, 1, 2, 1]
    print(f"Weighted average of {data1[:5]} with weights {weights}: {ps.weighted_average(data1[:5], weights):.2f}")
    
    print(f"Standard error of mean of {data1}: {ps.standard_error_mean(data1):.4f}")
    
    print("\n" + "=" * 60)
    print("2. MULTIVARIATE STATISTICS")
    print("-" * 30)
    
    print(f"\nData: x = {x}, y = {y}")
    
    print("\n2.1 CORRELATION")
    print(f"Pearson correlation: {ps.pearson_correlation(x, y):.4f}")
    print(f"Q-correlation: {ps.q_correlation(x, y):.4f}")
    
    print("\n2.2 COVARIANCE")
    print(f"Sample covariance: {ps.covariance(x, y):.4f}")
    print(f"Population covariance: {ps.covariance(x, y, population=True):.4f}")
    
    print("\n2.3 LINEAR REGRESSION")
    slope, intercept, r_squared = ps.linear_regression(x, y)
    print(f"Slope: {slope:.4f}")
    print(f"Intercept: {intercept:.4f}")
    print(f"R-squared: {r_squared:.4f}")
    print(f"Regression equation: y = {slope:.4f}x + {intercept:.4f}")
    
    print("\n2.4 SUMS")
    print(f"Sum of squared deviations (Sxx): {ps.sum_xx(x):.2f}")
    print(f"Sum of squared deviations (Syy): {ps.sum_yy(y):.2f}")
    print(f"Sum of products of deviations (Sxy): {ps.sum_xy(x, y):.2f}")
    
    print("\n" + "=" * 60)
    print("3. ADVANCED EXAMPLES")
    print("-" * 30)
    
    # Example with real-world data
    print("\n3.1 STUDENT GRADES ANALYSIS")
    math_scores = [85, 92, 78, 96, 88, 75, 90, 82, 95, 87]
    science_scores = [88, 90, 75, 94, 85, 72, 92, 80, 96, 89]
    
    print(f"Math scores: {math_scores}")
    print(f"Science scores: {science_scores}")
    
    print(f"\nMath Statistics:")
    print(f"  Mean: {ps.arithmetic_mean(math_scores):.2f}")
    print(f"  Median: {ps.median(math_scores):.2f}")
    print(f"  Standard deviation: {ps.standard_deviation(math_scores):.2f}")
    print(f"  Skewness: {ps.skewness(math_scores):.4f}")
    print(f"  Kurtosis: {ps.kurtosis(math_scores):.4f}")
    
    print(f"\nScience Statistics:")
    print(f"  Mean: {ps.arithmetic_mean(science_scores):.2f}")
    print(f"  Median: {ps.median(science_scores):.2f}")
    print(f"  Standard deviation: {ps.standard_deviation(science_scores):.2f}")
    print(f"  Skewness: {ps.skewness(science_scores):.4f}")
    print(f"  Kurtosis: {ps.kurtosis(science_scores):.4f}")
    
    print(f"\nCorrelation Analysis:")
    print(f"  Pearson correlation: {ps.pearson_correlation(math_scores, science_scores):.4f}")
    print(f"  Q-correlation: {ps.q_correlation(math_scores, science_scores):.4f}")
    
    slope, intercept, r_squared = ps.linear_regression(math_scores, science_scores)
    print(f"\nRegression Analysis:")
    print(f"  Slope: {slope:.4f}")
    print(f"  Intercept: {intercept:.4f}")
    print(f"  R-squared: {r_squared:.4f}")
    print(f"  Equation: Science = {slope:.4f} × Math + {intercept:.4f}")
    
    print("\n3.2 TIME SERIES ANALYSIS")
    monthly_sales = [100, 120, 110, 130, 125, 140, 135, 150, 145, 160, 155, 170]
    print(f"Monthly sales: {monthly_sales}")
    
    # Running average to smooth the data
    running_avg_3 = ps.running_average(monthly_sales, 3)
    running_avg_6 = ps.running_average(monthly_sales, 6)
    
    print(f"3-month running average: {[f'{x:.1f}' for x in running_avg_3]}")
    print(f"6-month running average: {[f'{x:.1f}' for x in running_avg_6]}")
    
    print(f"\nSales Statistics:")
    print(f"  Mean: {ps.arithmetic_mean(monthly_sales):.2f}")
    print(f"  Standard deviation: {ps.standard_deviation(monthly_sales):.2f}")
    print(f"  Coefficient of variation: {ps.standard_deviation(monthly_sales) / ps.arithmetic_mean(monthly_sales) * 100:.2f}%")
    
    print("\n" + "=" * 60)
    print("4. ERROR HANDLING EXAMPLES")
    print("-" * 30)
    
    print("\n4.1 Empty data:")
    try:
        ps.arithmetic_mean([])
    except ValueError as e:
        print(f"  Error: {e}")
    
    print("\n4.2 Non-numeric data:")
    try:
        ps.arithmetic_mean([1, "2", 3])
    except ValueError as e:
        print(f"  Error: {e}")
    
    print("\n4.3 Insufficient data for correlation:")
    try:
        ps.pearson_correlation([1], [2])
    except ValueError as e:
        print(f"  Error: {e}")
    
    print("\n4.4 Negative values for geometric mean:")
    try:
        ps.geometric_mean([1, -2, 3])
    except ValueError as e:
        print(f"  Error: {e}")
    
    print("\n" + "=" * 60)
    print("py-stats demonstration completed!")
    print("=" * 60)


if __name__ == "__main__":
    main() 