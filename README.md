# E-Commerce Product Delivery Prediction

## Overview

The E-Commerce Product Delivery Prediction project utilizes machine learning to predict whether a product from an e-commerce company will be delivered on time or not. The analysis also delves into various factors affecting delivery and studies customer behavior, providing valuable insights for the e-commerce business.

## Dataset

The dataset includes the following columns:

- ID
- Warehouse_block
- Mode_of_Shipment
- Customer_care_calls
- Customer_rating
- Cost_of_the_Product
- Prior_purchases
- Product_importance
- Gender
- Discount_offered
- Weight_in_gms
- Reached.on.Time_Y.N

## Insights

### Customer Demographics
- The dataset shows an almost equal distribution of male (49.6%) and female (50.4%) customers.

### Product Properties Distribution
- Weight Distribution: Products weighing between 1000-2000 grams and 4000-6000 grams are predominant.
- Product Importance: Most products have low or medium importance.
- Cost Distribution: The majority of products cost between 150-200 and 225-275 dollars.

### Logistic and Delivery Visualization
- Warehouse F has the highest number of products, possibly indicating proximity to a seaport.
- Most products are shipped via Ship, and timely deliveries outnumber late deliveries.

### Customer Experience Analysis
- Customer Care Calls: Majority of customers make 3-4 calls, possibly indicating issues with product delivery.
- Customer Rating: A slightly higher count in rating 1 suggests customer dissatisfaction.
- Prior Purchases: Customers with 2-3 prior purchases show satisfaction and tend to buy more.
- Discount Offered: Most products have 0-10% discount.

### Relationship Between Features
- No significant gender-based impact on timely product delivery.
- Weight and cost influence product delivery, with heavier and more expensive products showing a higher likelihood of delays.
- Logistic and mode of shipment have no significant impact on product delivery.

### Customer Behavior and Product Delivery
- More customer care calls correlate with a decrease in the difference between timely and late product delivery.
- Higher customer ratings are associated with timely product delivery.
- Customers with more prior purchases tend to have more products delivered on time.
- Products with higher discounts (>10%) show better on-time delivery.

## Machine Learning Models

- Decision Tree Classifier: Achieved the highest accuracy of 69%.
- Random Forest Classifier: Accuracy of 68%.
- Logistic Regression: Accuracy of 67%.
- K Nearest Neighbors: Lowest accuracy at 65%.

## Conclusion

The E-Commerce Product Delivery Prediction project provides valuable insights into customer behavior, logistics, and factors influencing timely deliveries. The machine learning models offer accurate predictions, with the Decision Tree Classifier performing the best. This project serves as a comprehensive analysis for the e-commerce business to enhance delivery services and customer satisfaction.

---