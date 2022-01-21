teksts = input("Ievadit tekstu: ")
def reverseWord(teksts):
  sar1 = teksts.split()
  if len(sar1)>1:
    sar1.reverse()
    teksts=""
    for elements in sar1:
      teksts+=elements
  else:
    teksts = "Pārāk īss teikums!"
    print(teksts)
  return teksts
reverseWord(teksts)