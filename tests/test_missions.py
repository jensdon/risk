import unittest
from entities.Missions import Missions


class MissionTest(unittest.TestCase):

    def setUp(self):
        self.missions_class = Missions()
        self.missions = []
        self.get_missions()

    def get_missions(self):
        mission = self.missions_class.get_mission()
        if mission:
            self.missions.append(mission)
            self.get_missions()

    def test_if_missions_are_unique(self):
        setlist = set()
        for mission in self.missions:
            setlist.add(mission)

        self.assertEqual(len(setlist),len(self.missions))


if __name__ == '__main__':
    unittest.main()