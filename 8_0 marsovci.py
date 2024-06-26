

krogi = [
    (164.4, 136.8, 50.8),
    (59.2, 182.8, 50.8),
    (282.8, 71.5, 45.6),
    (391, 229.4, 58.4),
    (259.9, 186, 47.6),
    (428, 89, 63.2),
    (88.6, 44.3, 37.5),
    (371.6, 233.6, 10.6),
    (408.7, 210.5, 8.9),
    (398.1, 95.5, 13),
    (449.5, 99.6, 13.6),
    (455.4, 66.5, 12.4),
    (139.6, 138, 10.6),
    (185, 138, 10.6),
    (69.8, 46.5, 10.6),
    (267.4, 51.7, 17.2),
    (225.8, 187.3, 7.5),
    (242.8, 187.3, 7.5),
    (259.8, 187.3, 7.5),
    (276.7, 187.3, 7.5),
    (293.7, 187.3, 7.5),
    (267.4, 51.7, 10.6),
    (99.6, 43.1, 17.2),
    (99.6, 43.1, 10.6),
    (150.3, 245.5, 50.8),
    (144.3, 243.6, 38.8),
    (127.3, 245.5, 7.5),
    (161.3, 245.5, 7.5)]
from math import sqrt
def ptici(krogi):
    slovar = {}

    #ce je not
    for krog1 in krogi:
        notranji_krogi =set( )
        for krog2 in krogi:
            if krog1 != krog2:
                koordinata1, koordinata2, polmer = krog1
                koordinata3, koordinata4, polmer2 = krog2
                razdalja = sqrt((koordinata1-koordinata3)**2 + (koordinata2-koordinata4)**2)
                if razdalja < polmer:
                    notranji_krogi.add((koordinata3, koordinata4))   #drugi je v prvm
                    slovar[koordinata1, koordinata2] = notranji_krogi
    s = set()
    for krog, vrednost in slovar.items():
        if len(vrednost) == 2 and slovar.get(list(vrednost)[0]) == None and slovar.get(list(vrednost)[1]) == None:
            s.add(krog)
    return (s)


def letala(krogi):
    je_ptic = ptici(krogi)
    slovar = {}
    for krog1 in krogi:
        notranji_krogi = set()
        for krog2 in krogi:
            if krog1 != krog2:
                koordinata1, koordinata2, polmer = krog1
                koordinata3, koordinata4, polmer2 = krog2
                razdalja = sqrt((koordinata1 - koordinata3) ** 2 + (koordinata2 - koordinata4) ** 2)
                if razdalja < polmer and polmer > polmer2:
                    notranji_krogi.add((koordinata3, koordinata4, polmer2))  # drugi je v prvm
                    slovar[koordinata1, koordinata2, polmer] = notranji_krogi

    l = set ()

    for krog, vrednost in slovar.items():
        ni_letalo = set()
        zunanji = True
        k1, k2, r = krog

        for x in slovar:
            if krog in slovar[x]:
                zunanji = False


        #print(krog, vrednost)
        for new in vrednost:
            if slovar.get(new) != None:
                    ni_letalo.add(krog)
                    #print("nl", len(ni_letalo), ni_letalo)
                    #print("nl",ni_letalo)

        if len(vrednost) != 2 and len(vrednost) != 0 and len(ni_letalo) == 0 and zunanji == True:
            l.add((k1, k2))

    return (l)





import time
import unittest


class TestObvezna(unittest.TestCase):
    def setUp(self):
        self.zacetek = time.time()

    def tearDown(self):
        self.assertLess(time.time() - self.zacetek, 15,
                        "vsak test se mora končati hitreje kot v 15 sekundah")

    def test_ptici(self):
        self.assertEqual({(164.4, 136.8), (391, 229.4)}, ptici(krogi))

        self.assertEqual(set(), ptici([(x, x, 0.5) for x in range(1000)]))

        self.assertEqual(set(), ptici([(0, 0, x) for x in range(1000)]))

        self.assertEqual(set(), ptici([(x, x, r)
                                       for x in range(30 * 100, 100)
                                       for r in range(30)]))

        self.assertEqual({(-100, -100)},
                         ptici([(-100, -100, 10),
                                (-102, -100, 1),
                                (-99, -100, 1)] +
                               [(x, x, r)
                                for x in range(30 * 100, 100)
                                for r in range(50)]))

    def test_letala(self):
        self.assertEqual({(259.9, 186), (428, 89)}, letala(krogi))

        self.assertEqual(set(), letala([(x, x, 0.5) for x in range(1000)]))
        self.assertEqual(set(), letala([(0, 0, x) for x in range(1000)]))

        self.assertEqual(set(), letala([(x, x, r)
                                        for x in range(30 * 100, 100)
                                        for r in range(30)]))

        self.assertEqual({(0, 0), (100000, 0),},
                         letala([(0, 0, 10000),
                                 (100000, 0, 1), (100000, 0, 0.5),
                                 (200000, 0, 1)]
                                + [(x, 0, 0.5) for x in range(1000)]))

        self.assertEqual({(100000, 0)},
                         letala([(0, 0, 10000),
                                 (100000, 0, 1), (100000, 0, 0.5),
                                 (200000, 0, 1)]
                                + [(x, 0, 0.5) for x in range(500)]
                                + [(x, 0, 0.3) for x in range(500)]))


"""class TestDodatna(unittest.TestCase):
    def setUp(self):
        self.zacetek = time.time()

    def tearDown(self):
        self.assertLess(time.time() - self.zacetek, 15,
                        "vsak test se mora končati hitreje kot v 15 sekundah")

    def test_sumljivi(self):
        self.assertEqual({(59.2, 182.8),
                          (88.6, 44.3),
                          (150.3, 245.5),
                          (282.8, 71.5)},
                         sumljivi(krogi))

        crta = [(x, x, 0.5) for x in range(1000)]
        self.assertEqual({(x, y) for x, y, _ in crta}, sumljivi(crta))


        self.assertEqual({(0, 0)}, sumljivi([(0, 0, x) for x in range(1000)]))

        crta = {(x, x, 29) for x in range(30 * 100, 100)}
        self.assertEqual(crta,
                         sumljivi([(x, x, r)
                                   for x in range(30 * 100, 100)
                                   for r in range(30)]))

        self.assertEqual(crta,
                         sumljivi([(-100, -100, 10),
                                   (-102, -100, 1),
                                   (-99, -100, 1)] +
                                  [(x, x, r)
                                   for x in range(30 * 100, 100)
                                   for r in range(50)]))

        self.assertEqual({(200000, 0),},
                         sumljivi([(0, 0, 10000),
                                   (100000, 0, 1), (100000, 0, 0.5),
                                   (200000, 0, 1)]
                                  + [(x, 0, 0.5) for x in range(1000)]))

        self.assertEqual({(0, 0), (200000, 0)},
                         sumljivi([(0, 0, 10000),
                                   (100000, 0, 1), (100000, 0, 0.5),
                                   (200000, 0, 1)]
                                  + [(x, 0, 0.5) for x in range(500)]
                                  + [(x, 0, 0.3) for x in range(500)]))
"""

if __name__ == "__main__":
    unittest.main()


