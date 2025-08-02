#!/usr/bin/env python3
"""
Advanced usage examples for py-stats package.

This script demonstrates the additional statistical functions
added to the py-stats package, including robust statistics,
order statistics, probability functions, and advanced multivariate analysis.
"""

import py_stats as ps

def main():
    """Main function demonstrating advanced py-stats usage."""
    
    print("=" * 70)
    print("py-stats: Advanced Statistics Package (v2.0)")
    print("=" * 70)
    
    # Sample datasets
    data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    data2 = [10, 20, 30, 40, 50]
    data3 = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    data_with_outliers = [1, 2, 3, 4, 5, 100, 200]  # Data with outliers
    
    # Multivariate data
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]
    
    # Categorical data for chi-square test
    observed_table = [[10, 20, 30], [15, 25, 35], [20, 30, 40]]
    
    print("\n1. ROBUST STATISTICS")
    print("-" * 30)
    
    print(f"\nOriginal data: {data_with_outliers}")
    print(f"Arithmetic mean: {ps.arithmetic_mean(data_with_outliers):.2f}")
    print(f"Winsorized mean (20%): {ps.winsorized_mean(data_with_outliers, 20):.2f}")
    print(f"Trimmed mean (20%): {ps.trimmed_mean(data_with_outliers, 20):.2f}")
    print(f"Interquartile range: {ps.interquartile_range(data_with_outliers):.2f}")
    print(f"Range: {ps.range_value(data_with_outliers):.2f}")
    print(f"Coefficient of variation: {ps.coefficient_of_variation(data_with_outliers):.2f}")
    
    print("\n2. ORDER STATISTICS")
    print("-" * 30)
    
    print(f"\nData: {data1}")
    print(f"Percentile rank of 5: {ps.percentile_rank(data1, 5):.1f}%")
    print(f"Percentile rank of 8: {ps.percentile_rank(data1, 8):.1f}%")
    
    deciles_result = ps.deciles(data1)
    print(f"Deciles: {[f'{d:.1f}' for d in deciles_result]}")
    
    print(f"25th percentile: {ps.percentile(data1, 25):.2f}")
    print(f"75th percentile: {ps.percentile(data1, 75):.2f}")
    print(f"90th percentile: {ps.percentile(data1, 90):.2f}")
    
    print("\n3. SHAPE AND DISTRIBUTION")
    print("-" * 30)
    
    print(f"\nData: {data1}")
    print(f"Coefficient of skewness: {ps.coefficient_of_skewness(data1):.3f}")
    print(f"Coefficient of kurtosis: {ps.coefficient_of_kurtosis(data1):.3f}")
    print(f"Appears normal? {ps.simple_normality_test(data1)}")
    
    # Test with skewed data
    skewed_data = [1, 1, 1, 2, 2, 3, 4, 5, 10, 20]
    print(f"\nSkewed data: {skewed_data}")
    print(f"Coefficient of skewness: {ps.coefficient_of_skewness(skewed_data):.3f}")
    print(f"Appears normal? {ps.simple_normality_test(skewed_data)}")
    
    print("\n4. CENTRAL TENDENCY ALTERNATIVES")
    print("-" * 30)
    
    print(f"\nData with outliers: {data_with_outliers}")
    print(f"Median: {ps.median(data_with_outliers):.2f}")
    print(f"Winsorized median (20%): {ps.winsorized_median(data_with_outliers, 20):.2f}")
    print(f"Midhinge: {ps.midhinge(data_with_outliers):.2f}")
    
    print("\n5. PROBABILITY AND DISTRIBUTION")
    print("-" * 30)
    
    print(f"\nData: {data1}")
    print(f"Z-score of 5: {ps.z_score(data1, 5):.3f}")
    print(f"T-score of 5: {ps.t_score(data1, 5):.3f}")
    print(f"Z-score of 8: {ps.z_score(data1, 8):.3f}")
    
    print(f"\nPercentile from z-score:")
    print(f"Z=0: {ps.percentile_from_z_score(0):.1f}%")
    print(f"Z=1: {ps.percentile_from_z_score(1):.1f}%")
    print(f"Z=1.96: {ps.percentile_from_z_score(1.96):.1f}%")
    
    # Confidence intervals
    ci_lower, ci_upper = ps.confidence_interval_mean(data1, 0.95)
    print(f"\n95% Confidence interval for mean: ({ci_lower:.2f}, {ci_upper:.2f})")
    
    ci_lower, ci_upper = ps.confidence_interval_proportion(8, 10, 0.95)
    print(f"95% Confidence interval for proportion (8/10): ({ci_lower:.3f}, {ci_upper:.3f})")
    
    print("\n6. TIME SERIES ANALYSIS")
    print("-" * 30)
    
    time_series = [10, 12, 15, 14, 16, 18, 17, 19, 20, 22]
    print(f"Time series: {time_series}")
    
    moving_avg = ps.moving_average(time_series, window=3)
    print(f"Moving average (window=3): {[f'{x:.1f}' for x in moving_avg]}")
    
    exp_smooth = ps.exponential_smoothing(time_series, alpha=0.3)
    print(f"Exponential smoothing (α=0.3): {[f'{x:.1f}' for x in exp_smooth]}")
    
    # Seasonal decomposition (simple example)
    seasonal_data = [10, 15, 20, 25, 12, 17, 22, 27, 14, 19, 24, 29]
    trend, seasonal, residual = ps.seasonal_decomposition_simple(seasonal_data, period=4)
    print(f"\nSeasonal decomposition (period=4):")
    print(f"Trend: {[f'{x:.1f}' for x in trend[:4]]}...")
    print(f"Seasonal: {[f'{x:.1f}' for x in seasonal[:4]]}...")
    print(f"Residual: {[f'{x:.1f}' for x in residual[:4]]}...")
    
    print("\n7. ADVANCED MULTIVARIATE ANALYSIS")
    print("-" * 30)
    
    print(f"\nVariables: x={x}, y={y}")
    print(f"Pearson correlation: {ps.pearson_correlation(x, y):.3f}")
    print(f"Spearman correlation: {ps.spearman_correlation(x, y):.3f}")
    print(f"Kendall's tau: {ps.kendall_tau(x, y):.3f}")
    
    # Point-biserial correlation
    continuous_var = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    binary_var = [True, False, True, False, True, False, True, False, True, False]
    print(f"\nPoint-biserial correlation:")
    print(f"Continuous: {continuous_var}")
    print(f"Binary: {binary_var}")
    print(f"Correlation: {ps.point_biserial_correlation(continuous_var, binary_var):.3f}")
    
    print("\n8. REGRESSION ANALYSIS")
    print("-" * 30)
    
    # Simple linear regression
    slope, intercept, r_squared = ps.linear_regression(x, y)
    print(f"Simple linear regression:")
    print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")
    print(f"R-squared: {r_squared:.3f}")
    
    # Residual analysis
    residuals, r_sq, adj_r_sq = ps.residual_analysis(x, y)
    print(f"Residual analysis:")
    print(f"Residuals: {[f'{r:.2f}' for r in residuals]}")
    print(f"R-squared: {r_sq:.3f}")
    print(f"Adjusted R-squared: {adj_r_sq:.3f}")
    
    # Polynomial regression
    poly_coeffs, poly_r_sq = ps.polynomial_regression(x, y, degree=2)
    print(f"\nPolynomial regression (degree=2):")
    print(f"Coefficients: {[f'{c:.2f}' for c in poly_coeffs]}")
    print(f"R-squared: {poly_r_sq:.3f}")
    
    print("\n9. ASSOCIATION MEASURES")
    print("-" * 30)
    
    print(f"Observed frequency table:")
    for row in observed_table:
        print(f"  {row}")
    
    chi_sq, p_value, df = ps.chi_square_test(observed_table)
    print(f"Chi-square test:")
    print(f"  Chi-square statistic: {chi_sq:.3f}")
    print(f"  p-value: {p_value:.3f}")
    print(f"  Degrees of freedom: {df}")
    
    cramer_v = ps.cramers_v(observed_table)
    print(f"Cramer's V: {cramer_v:.3f}")
    
    contingency_coeff = ps.contingency_coefficient(observed_table)
    print(f"Contingency coefficient: {contingency_coeff:.3f}")
    
    print("\n10. COMPARISON OF DIFFERENT MEASURES")
    print("-" * 30)
    
    print(f"\nData: {data1}")
    print(f"Arithmetic mean: {ps.arithmetic_mean(data1):.2f}")
    print(f"Geometric mean: {ps.geometric_mean(data1):.2f}")
    print(f"Harmonic mean: {ps.harmonic_mean(data1):.2f}")
    print(f"Quadratic mean: {ps.quadratic_mean(data1):.2f}")
    print(f"Median: {ps.median(data1):.2f}")
    print(f"Trimean: {ps.trimean(data1):.2f}")
    print(f"Midrange: {ps.midrange(data1):.2f}")
    
    print(f"\nDispersion measures:")
    print(f"Variance: {ps.variance(data1):.2f}")
    print(f"Standard deviation: {ps.standard_deviation(data1):.2f}")
    print(f"Average deviation: {ps.average_deviation(data1):.2f}")
    print(f"Median absolute deviation: {ps.median_absolute_deviation(data1):.2f}")
    print(f"Interquartile range: {ps.interquartile_range(data1):.2f}")
    print(f"Range: {ps.range_value(data1):.2f}")
    print(f"Coefficient of variation: {ps.coefficient_of_variation(data1):.3f}")
    
    print("\n11. ERROR HANDLING EXAMPLES")
    print("-" * 30)
    
    try:
        ps.arithmetic_mean([])
    except ValueError as e:
        print(f"Empty data error: {e}")
    
    try:
        ps.harmonic_mean([1, -2, 3])
    except ValueError as e:
        print(f"Negative values in harmonic mean: {e}")
    
    try:
        ps.pearson_correlation([1, 2, 3], [1, 2])
    except ValueError as e:
        print(f"Mismatched lengths: {e}")
    
    try:
        ps.chi_square_test([[1], [2]])
    except ValueError as e:
        print(f"Invalid chi-square table: {e}")
    
    print("\n" + "=" * 70)
    print("Advanced py-stats demonstration completed!")
    print("This package now includes over 60 statistical functions")
    print("perfect for educational and small-scale statistical analysis.")
    print("=" * 70)

if __name__ == "__main__":
    main() 