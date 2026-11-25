## Ievade
1. speletaja_vards = int(input("Ievadi savu vārdu: "))
2. speletaja_gads = int(input("Ievadi dzimšanas gadu: "))
3. izveletais_gads  = int(input("Kurš gads tev interesē?: "))

## Apstrāde
4. rezultats = (izveletais_gads - speleteja_gads)

## Izvade
5. print(f"Sveicināts gadu aprēķinā! Ievadi gadaskaitli, un uzzini cik tev būs gadi!")
6. print(f"tev {izveletais_gads} būs {rezultats} gadi!")


| Mainīgā vārds | Datu tips | Ko glabā |
| :--- | :---: | ---: |
|speletaja_vards|Str|vārdu|
|izveletais_gads|Int|Izvēlēto gadu|
|speleteja_gads|Int|dzimšanas gadu|
|rezultats|Float|rezultātu|

rezultats = (input4 - input2)

no input nāk spēlētaja vecums, gads un izvēlētais gads, tiek aprēķināts rezultāts.

rez. rēķinot ar galvu:
s.g. - 2009
i.g. - 2027
s.v. - 17
rezultats = (2027 - 2009)=18