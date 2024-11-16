# Project Instructions🧪

## Table of Contents 📑
1. [Instructions](#instructions)
2. [Example Solution](#example-solution)
3. [Data Generation](#data-generation)
4. [Linear Regression](#linear-regression)
5. [Results and Data Pairs](#results-and-data-pairs)
6. [Plots](#plots)

---

## Instructions🎯

- Manually generate several images containing points that show a correlation (at least one image with an ascending slope and at least one with a descending slope).
- In Python, determine the pairs of points (xᵢ, yᵢ) from the images.
- Calculate and display the values of *a*, *b*, and *Q(a,b)* according to the formulas.
- Draw the trend line on the images using a different color.

---

## Example Solution💡

1. **Data Generation**: We use the `np.random.uniform` function to generate 30 random points for each dataset. For the ascending slope, `x_asc` is generated between 1 and 40, and `y_asc` is calculated using the equation of a line with a positive slope. For the descending slope, `x_desc` is generated between 1 and 40, and `y_desc` is calculated using the equation of a line with a negative slope.
   
2. **Linear Regression**: The `linear_regression` function receives the datasets `x` and `y` as arguments and returns the coefficients *a* and *b* of the regression line equation, as well as the predicted *y* values based on these coefficients and the total regression error.

3. **Displaying Results and Data Pairs**: The coefficients *a* and *b*, as well as the total error for each dataset, are displayed. Then, each data pair (xᵢ, yᵢ) for both datasets is shown.

---

## Data Generation📊

<div style="text-align: center;">
    <h3>Ascending Slope Data Points:</h3>
    <table style="margin: 0 auto;">
        <tr>
            <th>Point</th>
            <th>Coordinates</th>
        </tr>
        <tr>
            <td>1</td>
            <td>(22.403726653165666, 51.71245585103955)</td>
        </tr>
        <tr>
            <td>2</td>
            <td>(28.89238528852436, 87.62528660158847)</td>
        </tr>
        <tr>
            <td>3</td>
            <td>(24.50777166679411, 64.5423082833329)</td>
        </tr>
        <tr>
            <td>4</td>
            <td>(22.25044413687898, 65.08041597284713)</td>
        </tr>
        <tr>
            <td>5</td>
            <td>(17.522537174217284, 30.89061536807055)</td>
        </tr>
        <tr>
            <td>6</td>
            <td>(26.18987040959959, 75.17333818761364)</td>
        </tr>
        <tr>
            <td>7</td>
            <td>(18.065901239245008, 58.676110000998975)</td>
        </tr>
        <tr>
            <td>8</td>
            <td>(35.779147030501115, 94.32032392036629)</td>
        </tr>
        <tr>
            <td>9</td>
            <td>(38.58284765954014, 114.63435885223836)</td>
        </tr>
        <tr>
            <td>10</td>
            <td>(15.95421923420533, 57.59035192806742)</td>
        </tr>
        <tr>
            <td>11</td>
            <td>(31.87727648522392, 74.93240849626821)</td>
        </tr>
        <tr>
            <td>12</td>
            <td>(21.626901870363273, 57.92024166169691)</td>
        </tr>
        <tr>
            <td>13</td>
            <td>(23.15373788266336, 72.70087958205364)</td>
        </tr>
        <tr>
            <td>14</td>
            <td>(37.09826889341378, 71.9066840101447)</td>
        </tr>
        <tr>
            <td>15</td>
            <td>(3.770406269717591, 32.545314734490226)</td>
        </tr>
        <tr>
            <td>16</td>
            <td>(4.398042688360087, 33.974789509537345)</td>
        </tr>
        <tr>
            <td>17</td>
            <td>(1.788517500172703, 8.044250248668247)</td>
        </tr>
        <tr>
            <td>18</td>
            <td>(33.47217397636958, 67.74603134720756)</td>
        </tr>
        <tr>
            <td>19</td>
            <td>(31.348113287044168, 71.89050236567661)</td>
        </tr>
        <tr>
            <td>20</td>
            <td>(34.93047378162595, 81.22793225566991)</td>
        </tr>
        <tr>
            <td>21</td>
            <td>(39.1661153470778, 98.99108536296018)</td>
        </tr>
        <tr>
            <td>22</td>
            <td>(32.167184004452224, 79.07143611470886)</td>
        </tr>
        <tr>
            <td>23</td>
            <td>(18.997695127864343, 77.47221296839386)</td>
        </tr>
        <tr>
            <td>24</td>
            <td>(31.440637875171763, 62.47329223400479)</td>
        </tr>
        <tr>
            <td>25</td>
            <td>(5.612702608888395, 15.624859242044352)</td>
        </tr>
        <tr>
            <td>26</td>
            <td>(25.95691983177343, 54.17276796837169)</td>
        </tr>
        <tr>
            <td>27</td>
            <td>(6.59077820895281, 37.57143106384855)</td>
        </tr>
        <tr>
            <td>28</td>
            <td>(37.84208776493377, 82.08229764415773)</td>
        </tr>
        <tr>
            <td>29</td>
            <td>(21.352084548252794, 58.688153875039376)</td>
        </tr>
        <tr>
            <td>30</td>
            <td>(17.17181565963042, 40.34278295933296)</td>
        </tr>
    </table>
    
    <h3>Descending Slope Data Points:</h3>
    <table style="margin: 0 auto;">
        <tr>
            <th>Point</th>
            <th>Coordinates</th>
        </tr>
        <tr>
            <td>1</td>
            <td>(7.199813762175269, 74.93597533595903)</td>
        </tr>
        <tr>
            <td>2</td>
            <td>(5.3046305054079, 94.42420608754988)</td>
        </tr>
        <tr>
            <td>3</td>
            <td>(26.596853989145664, 27.73719582990632)</td>
        </tr>
        <tr>
            <td>4</td>
            <td>(6.389135102595938, 94.45645398014358)</td>
        </tr>
        <tr>
            <td>5</td>
            <td>(8.666712105522087, 70.68984997157987)</td>
        </tr>
        <tr>
            <td>6</td>
            <td>(15.3802816557776, 52.48304797876506)</td>
        </tr>
        <tr>
            <td>7</td>
            <td>(33.01873596406947, 35.3556101383148)</td>
        </tr>
        <tr>
            <td>8</td>
            <td>(4.78694975592939, 66.33094006657842)</td>
        </tr>
        <tr>
            <td>9</td>
            <td>(33.67985139245335, 44.94259852987464)</td>
        </tr>
        <tr>
            <td>10</td>
            <td>(4.747837907864559, 65.71562061293551)</td>
        </tr>
        <tr>
            <td>11</td>
            <td>(39.08191913552243, 27.33790588478549)</td>
        </tr>
        <tr>
            <td>12</td>
            <td>(19.27739686426036, 48.5955650651267)</td>
        </tr>
        <tr>
            <td>13</td>
            <td>(39.09368243942315, 29.89636611667047)</td>
        </tr>
        <tr>
            <td>14</td>
            <td>(24.588975270056793, 69.12053399017114)</td>
        </tr>
        <tr>
            <td>15</td>
            <td>(29.831279596533765, 26.531332265330583)</td>
        </tr>
        <tr>
            <td>16</td>
            <td>(2.528323897918506, 95.87043225296566)</td>
        </tr>
        <tr>
            <td>17</td>
            <td>(12.029471540479975, 77.58294382627281)</td>
        </tr>
        <tr>
            <td>18</td>
            <td>(5.687665887313587, 89.37600398596213)</td>
        </tr>
        <tr>
            <td>19</td>
            <td>(12.549467703363652, 59.93973806210052)</td>
        </tr>
        <tr>
            <td>20</td>
            <td>(16.39175958663694, 98.16219124270784)</td>
        </tr>
        <tr>
            <td>21</td>
            <td>(11.021240300306005, 77.53259654023292)</td>
        </tr>
        <tr>
            <td>22</td>
            <td>(38.77415450304509, 43.6881313782419)</td>
        </tr>
        <tr>
            <td>23</td>
            <td>(5.586647846350108, 96.01766269985093)</td>
        </tr>
        <tr>
            <td>24</td>
            <td>(32.182141129183055, 54.69566535133639)</td>
        </tr>
        <tr>
            <td>25</td>
            <td>(15.51047816292623, 84.04819861815585)</td>
        </tr>
        <tr>
            <td>26</td>
            <td>(35.5373074177275, 77.1161613452477)</td>
        </tr>
        <tr>
            <td>27</td>
            <td>(28.46391105771014, 42.46809682821527)</td>
        </tr>
        <tr>
            <td>28</td>
            <td>(3.6901476762235365, 97.8274076037609)</td>
        </tr>
        <tr>
            <td>29</td>
            <td>(12.499187186647122, 93.7463806974564)</td>
        </tr>
        <tr>
            <td>30</td>
            <td>(35.13704623288508, 50.76421351746603)</td>
        </tr>
    </table>
</div>

---

## Linear Regression📐

- **Ascending Slope**:
  - Coefficient *a*: 17.6293
  - Coefficient *b*: 1.9027
  - Total Error: 3837.8738

- **Descending Slope**:
  - Coefficient *a*: 94.8914
  - Coefficient *b*: -1.7545
  - Total Error: 4421.7837

---

## Results and Data Pairs📝

- **Displaying the coefficients a and b** for both ascending and descending datasets along with the total errors.
- **Point pairs for both datasets** are provided above.

---

## Plots📊

- **Visualization** of both the data points and the trend lines is presented in the form of plots. The trend lines will be clearly visible in contrasting colors to indicate the direction of the relationship between the points.

<p align="center">
  <img src="ex1.png" alt="something" width="700">
  <br>
  <em>Linear Regression: Ascending Slope</em>
  <br>
  <br>
  <img src="ex2.png" alt="something" width="700">
  <br>
  <em>Linear Regression: Descending Slope</em>
</p>