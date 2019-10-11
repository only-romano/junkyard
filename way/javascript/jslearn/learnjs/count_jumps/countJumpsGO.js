def countWays(m_jumps, steps):
	variants = []

	for a in range(steps, 1, -1):
		var = [1] * a
		if sum(var) == steps:
			variants.append(' - '.join(str(x) for x in var))
			continue
		if m_jumps > 1:

			for c in range(0, a):
				var2 = var[:]
				for b in range(2, m_jumps + 1):
					var2[c] = b
					if sum(var2) == steps and var2 not in variants:
						variants.append(' - '.join(str(x) for x in var2))
						break

					elif c + 1 != a:

						for d in range(c + 1, a):
							var3 = var2[:]
							for e in range(2, m_jumps + 1):
								var3[d] = e
								if sum(var3) == steps and var3 not in variants:
									variants.append(' - '.join(str(x) for x in var3))
									break
							else:
								break
	print('Количество вариантов: ', len(variants))
	print('Все возможные варианты: \n', '\n'.join(variants))
			
		
countWays(3,7)
#Первый параметр - K, второй - N