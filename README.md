# Final Project, the Prime(r)nator, a primer designing tool with a GUI.
#
# STEPS FOR GENERAL USE
##   1. Put the entire sequence you are trying to amplify
##   2. Enter the sequence of the region in which you would like the forward primer to be designed. Leave this line empty if you are indifferent about where the forward primer is designed.
##   3. Enter the sequence of the region in which you would like the reverse primer to be designed. Leave this line empty if you are indifferent about where the reverse primer is designed
##   4. Enter values for the minimum and maximum sizes you would like for your final amplicon, or leave blank if you are indifferent.
##   5. Hit the 'Get Primers' button to view a list of the top 10 best primer combinations! (primer combos are rank ordered based on Tm similarity)
##
## In addition, the prime(r)nator includes multiple options to create more perfect primers. Access these settings in the 'settings' menu.
##
# OPTIONAL SETTINGS
## Primer Length: The minimum and maximum lengths the primer sequences can be.

## Tm: The minimum and maximum melting temperatures for your primers. Melting temperature is calculated according to the values provided in SantaLucia (1998).

## Max Tm Difference: The maximum difference allowed in the melting temperature of your forward and reverse primers. In most cases this setting does not need altering but is set by default to 5 Celsius.

## GC content: The minimum and maximum allowed GC content of the primers. Default is a minimum of 40% and a maximum of 60%.

## First base must be A or T: Whether the 5' base must be an A or a T. Turned off by default.

## Last base must be G or C: Whether the 3' base must be a G or a C. Turned on by default, and not recommended to turn off.

## Avoid Repetition: Determines whether primers with repetitive regions should be excluded.

## Define 'repetitive': Enter a value for how many consecutive bases must be identical to be considered reptitive.

## #G or C in last 6 bases: Defines how many of the last 6 bases on the 3' side of the primer must be a G or C.

## Salt Concentration: The salt concentration in your PCR, unit is Molar. Salt concentration affects the melting temperature of your primers.

## All settings are saved in real time. All entries must be numbers, otherwise the setting will restore to its default value. The 'Restore Defaults' button does just as the name implies; it restores the value of all settings to their defaults.
