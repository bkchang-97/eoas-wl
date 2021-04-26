---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.7.1
---


# Slide 0
```

Today’s Class
1
R&R – review and reinforcement  – from last time
Earth’s Radiation Balance: Incoming solar radiation and albedo – how they compare to thermal emission/absorption

```




# Slide 1
```

R&R:
Power, Energy flux, black bodies and gray bodies
2
Assume the initial temperature of the coffee, T, is the same in each cup

```




# Slide 2
```

R&R:  Power
PS > PT > PG > PV
PV > PG > PT > PS
PV = PG = PT = PS
3
Which of the following is true about the initial power (heat) output from each of the cups of coffee?
Assume the initial temperature of the coffee, T, is the same in each cup

```




# Slide 3
```

J
Js
J s-1
J s-1 m-2
W m-2
4
What are the units of power?
R&R:  Power

```




# Slide 4
```

5
Which of the following is true about the energy flux from each of the cups of coffee?
(hint: remember the units of energy flux)
R&R:  Energy Flux
ES > ET > EG > EV
EV > EG > ET > ES
EV = EG = ET = ES

```




# Slide 5
```

Day 3 worksheet, #1
6
TL = 280 K
Is there a net transfer of energy from
Right to Left
Left to Right
Not at all
TR = 280 K

```




# Slide 6
```

Day 3 worksheet, #2
7
TL = 280 K
TR = 280 K
Which wall changes its temperature with time?
Right
Left
Neither
Both

```




# Slide 7
```

Day 3 worksheet, #3
8
TL = 280 K
TR = 280 K
Which wall will emit the most radiative flux?
Right
Left
e = 0.6
e = 1.0

```




# Slide 8
```

Day 3 worksheet, #4
9
TL = 280 K
TR = 280 K
e = 0.6
e = 1.0
Iemit_R

```




# Slide 9
```

Day 3 worksheet, #5
10
TL = 280 K
TR = 280 K
e = 0.6
e = 1.0
Iemit_R
Iemit_R
Iemit_L
Irefl_L
At the LH wall Iemit_R > Iemit_L so some flux must be reflected, or temperature of
LH wall would change, in violation of the 2nd law of thermodynamics
So 2nd law requires:  Irefl-L + Iemit-L = Iemit_R

```




# Slide 10
```

Notes about emissivity:
Just because a body in equilibrium emits the same amount of flux as it absorbs does not mean that the outgoing radiation will be at the same wavelength (e.g. the ocean absorbs shortwave radiation and emits longwave radiation).
Different surfaces/layers have different colors because their reflectivity changes with wavelength.  For the same reason, their emissivites and absorptivities also change with wavelength.
11

```




# Slide 11
```

Grey body radiation
‘Grey body’ is an approximation for a real body whose emission is different from a black body in a way that depends on wavelength.
We approximate this by a constant factor, the broadband emissivity, e, that is the ratio of the area under the true grey body curve c.f. area under the black body curve.  Grey body energy flux = esT4
12

```




# Slide 12
```

13
R&R:  Black body spectrum
BTW: this figure shows that the actual spectrum (black) of the Sun really looks like that of a black body (green curve) with a temperature T ~ 5800 K

```




# Slide 13
```

Power
Energy flux
Neither of the above
idk
14
What corresponds to the area under this curve?
Black body spectrum
BTW: this figure shows that the actual spectrum (black) of the Sun really looks like that of a black body (green curve) with a temperature T ~ 5800 K

```




# Slide 14
```

BB with different T
15
As T increases
Peak of BB spectrum moves to shorter wavelength (or bigger wavenumber – see last time). Remember from the text book, the peak is at a wavelength of 2897/T (T in Kelvin) in mm. Check these peaks for yourself – my T = 5°C for mud, 37°C for Arnold and 80°C for hot coffee.
Curve has higher intensity at all wavelengths, so area under curve increases – we know it must b/c area under curve is equal to sT4

```




# Slide 15
```

Greybodies: An approximation
Most real objects do NOT emit equally well at all wavenumbers (although water comes close in the longwave).
Instead, real objects radiate a fraction of the EM energy an ideal black body at the same temperature would radiate
We call this the “greybody” approximation:
I = εσT4
This is the RATIO of the actual energy emitted I to that which a blackbody would emit
16

```




# Slide 16
```

Greybodies: An approximation
Total blackbody flux (area):
This object only emits in the green wavenumber band. Green Area is 95 W/m2
The greybody emissivity is:
ε = 95/188 = 0.5
T=240 K
17

```




# Slide 17
```

T=300 K
Total blackbody flux (area):
This object only emits in the green wavenumber band. Green Area is 227 W/m2
The greybody emissivity is:
ε = 227/460 = 0.5
σT4 = 460 W/m2
Emissivity is NOT a function of temperature
18

```




# Slide 18
```

Grey body radiation
19
True
False
The emissivity of a gray body must be less than 1.

```




# Slide 19
```

Black vs. grey bodies
What is the point of the greybody approximation?  We get to ignore the details of the complex absorption/emission bands, and approximate their effect by a single number, the greybody emissivity e.  In climate models the radiation calculations typically use about 20-30 bands spanning the long and short wavelengths.
20

```




# Slide 20
```

The world in the infrared
IR vs. visible video
Crucial point – at 2:30 he puts a sheet of paper (cold) over his face (hot) – note that the paper absorbs the IR flux from his face and emits much less – it is absorbing radiation and heating up.  This is the definition of the greenhouse effect.
21

```




# Slide 21
```

The story so far:
22

```




# Slide 22
```

Goals:
Apply systems dynamics concepts of stock and flow to Earth’s energy budget.   dE/dt = Idown + Iup  = Idown - |Iup|
Figure out the incoming solar radiation for Earth and other planets
Compare reflectivity of different parts of the Earth system, both on the surface and in the atmosphere.
Predict the impacts of altering solar energy or reflectivity on flows of energy in Earth's climate system, and therefore Earth's temperature (left side of Earth's energy budget diagram)
Classify particular changes in incoming solar radiation and albedo as forcings or feedbacks.
Calculate planetary temperature response to an instantaneous forcing due to the Planck feedback alone.
Day 4: Earth’s Radiation Balance
Incoming solar radiation and albedo
23

```




# Slide 23
```

Earth’s Climate - A Stock & Flow analogy
24
The stock (volume of water) in the bathtub changes according to:
dV/dt = Iin - Iout
where the outflow depends on the current stock:
Iout = (const) x h
The “Bathtub” Balance
*notice the feedback mechanism*

```




# Slide 24
```

Earth’s Climate - A Stock & Flow analogy
25
The stock (volume of water) in the bathtub changes according to:
dV/dt = Iin - Iout
where the outflow depends on the current stock:
Iout = (const) x h
The “Bathtub” Balance

```




# Slide 25
```

How much energy does the Earth receive from the Sun???
Let’s calculate the solar constant (use pen & paper)
Need following information
Sun outputs 3.8 x 1026 W   (1W = 1J/s)
Mean sun-earth distance is 150 x 109 m
Area of the distance-sphere is 2.8 x 1023 m2
Energy received at the Earth is known as the “solar constant” and is   S = 1,360 W/m2
How much energy does the Earth absorb? Need radius of the earth  R = 6.4 x 106 m
26

```




# Slide 26
```

Image credit: NASA
Solar constant is 1360 W/m2
At the top of the atmosphere directly facing the Sun, Earth receives 1360 W/m2
The Earth “blocks” an area in space equal to the area of a circle with Earth’s radius (pR2)
Each square meter of that imaginary circle gets 1360 W
Total energy received proportional to area of that circle
The TOTAL energy Earth captures is  1360 x pR2   [W]
Distribute total energy received over the surface area of the Earth: (1360 x pR2) / 4pR2   =  1360 / 4  =  340 [W/m2].
Aside: Trenberth was working with about 1365 W/m2 for the solar constant 341 W/m2
27

```




# Slide 27
```

CLICKER: Earth’s radiation balance
28
If the distance between the Earth and the Sun doubles
AND
the radius of the Earth shrinks to half its current value,
how will the amount of radiation per unit area (W/m2) received at the surface of the Earth change?
A. Decreases by a factor of 2
B. Decreases by a factor of 4
C. Decreases by a factor of 8
D. Decreases by a factor of 16

```




# Slide 28
```

CLICKER: Heating rates? 
At what rate does this atmosphere (the area between the lines) heat up (+) or cool down (-)?
29
-10 Wm-2
-20 Wm-2
+20 Wm-2
+50 Wm-2
+70 Wm-2

```




# Slide 29
```

Worksheet: The Earth as a Stock and Flow Problem
30

```




# Slide 30
```

Focus on Albedo – left side of diagram
31

```




# Slide 31
```

Summary
Balances of flows of energy in, out, and within Earth’s climate system determine Earth’s temperature.
We use the “grey body approximation” to estimate the emissivity/absorptivity of the atmosphere
Kirchoff’s law guarantees that ε=abs because otherwise we violate the 2nd law of thermodynamics
Solids, liquids and gasses emit radiation according to their temperature and their emissivity via the Stefan-Boltzman equation:  I = εσT4
These same objects absorb radiation with constant abs=ε that is independent of temperature.
That means that cold air can absorb radiation from a warm surface, but not re-radiate all that it has absorbed  This is heating because of the imbalance is called the “greenhouse effect”
This doesn’t violate the 2nd law because this system is not isolated – the surface is warmer that the atmosphere because it is absorbing sunlight that passes straight through air.
32

```




# Slide 32
```

“If we were to approximate the average albedo of each of the hemispheres of the Earth, would we get significantly similar quantities?”
image: NASA
Earth’s surface if the planet were cloud-free
Which parts of the Earth are MORE reflective?
Which parts of the Earth are LESS reflective?
What is the single largest reason that the Earth’s albedo is relatively LOW?
33

```




# Slide 33
```

34

```




# Slide 34
```

NASA
CLICKER: What if the forest expanded into the desert area (and nothing else changed)?
Reflectivity would _______.
NASA
A. Increase       B. Decrease       C. Stay the same
35

```




# Slide 35
```

NASA
CLICKER: What if sea level rose (and nothing else changed)? Reflectivity would _______.
NASA
A. Increase       B. Decrease       C. Stay the same
36

```




# Slide 36
```

Some  Surface Albedos
NASA
From http://www.eoearth.org/view/article/149954/
Compare these
37

```




# Slide 37
```

Cloud Albedo is Variable
NASA
THICK: more reflective (0.5-0.7)
THIN: less reflective (0.1-0.5)
38
Cloud reflectivity is one of the big unknowns that make predictions about future climate uncertain.  Will future cloud albedos be bigger or smaller?
The reflectivity of clouds is determined by water droplet density AND droplet size. Drop-for-drop, smaller drops have larger surface area to volume ratio. 
More SA = greater reflectivity.

```




# Slide 38
```

Aerosol Albedo -
NASA
MORE reflective: Sea salt particles, Sulfate aerosols, Mineral dust
LESS reflective: Black carbon (ie. “soot”)
39

```




# Slide 39
```

CLICKER: What if sunspots change incoming solar radiation?
A. Forcing        B. Feedback        C. Could be either
40

```




# Slide 40
```

CLICKER: What if ice on Earth’s surface melts?
A. Forcing        B. Feedback        C. Could be either
41

```




# Slide 41
```

CLICKER: What if coal-burning increases sulfate aerosols?
A. Forcing        B. Feedback        C. Could be either
42

```




# Slide 42
```

IDENTIFY: “Amplifying” or “Stabilizing”
Necessary to distinguish between two types of feedback mechanisms:
The initial perturbation is dampened by the feedback mechanism  STABILIZING (negative)
The initial change (perturbation) is continually amplified by the feedback mechanism  AMPLIFYING (positive)
We will revisit this on Day 11 - For now, let’s do some practice
43

```




# Slide 43
```

CLICKER:  Clouds are involved in several different feedbacks.  Is this one amplifying or stabilizing?
Warming
More 
water in a warmer atmosphere
Greater cloud low cover
Greater reflectivity
?
Perturbation
A. Amplifying
B. Stabilizing
C. Could be either
?
44

```




# Slide 44
```

Warming
More 
water in a warmer atmosphere
Greater cloud cover
Greater reflectivity
Cooler temperatures counteract warming
Perturbation
Stabilizing!
45

```




# Slide 45
```

CLICKER:  The Planck Feedback.  Amplifying or Stabilizing?
A. Amplifying
B. Stabilizing
C. Could be either
46

```




# Slide 46
```

CLICKER:  The Planck Feedback.  Amplifying or Stabilizing?
Decrease energy inflow
Imbalance of inflow and outflow of energy
Earth’s temperature ???
Radiation
emitted ???
???
Perturbation
???
A. Amplifying
B. Stabilizing
C. Could be either
47

```




# Slide 47
```

The Planck Feedback:  Amplifying or Stabilizing?
48

```




# Slide 48
```

Temperature and sea ice trends due to both forcings (CO2, aerosols) and weather (wind patterns)
aerosol cooling
wind transport through Fram strait
49

```




# Slide 49
```

unused
50

```




# Slide 50
```

51
I am confused about question 3. Why do we need to average over the total surface area of the Earth to do this question?? The numbers given are already the averages.
How is the radius from the sun a determining factor in the solar constant?
Can you go over the calculations in more detail during class? We can do that
Why is it ok to assume that the earth's albedo is 0.3, when the surface areas of the different parts of Earth are so different (i.e. ALL desert, ALL snow, some land, some snow etc...)?   Averaging - it’s a model
If we were to approximate the average albedo of each of the hemispheres of the Earth, would we get significantly similar quantities?  Let’s come back to this
As well, why are power and energy used interchangeably in climate calculations? Which symbols do I use?  Context matters - be flexible - check units
Question 4 was difficult, I had difficulty understanding what the question was asking and how to approach it.  Do it at the end of class, IF we have time
How was Stefan Boltzmann inspired to study this?
Josef Stefan  and  Ludwig Boltzman
Day 4 PreClass Quiz Feedback

```




# Slide 51
```

The Planck Feedback (I)
FIRST:  No sun  Earth emits 0.06 W/m2 (geothermal source)
Recall: σ = 5.67 x 10-8 W/m2/K.  Assume ε = 1.  No atmosphere.
CLICKER:  What is Earth’s temperature?
A.   About 6 K
B.   About 32 K
C.   About 112 K
D.   About 273K
52

```




# Slide 52
```

NEXT:  Turn on Sun
Suddenly, Earth receives 341 W/m2.
Albedo = 0.3
No atmosphere
Assume ε = 1
CLICKER:  What will happen?
Earth will immediately become 278 K
Earth will warm, over time, to 278 K
Earth will immediately become 255 K
Earth will warm, over time, to 255K
Earth will warm up, but we can’t tell how much.
53

```

