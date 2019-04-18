import java.util.ArrayList;

import java.util.*;

import java.io.*;

public class AllPaths

{

	private final Map<String, TreeSet<DistanceTo>> cities = new HashMap<String, TreeSet<DistanceTo>>();

	void createGraph() throws FileNotFoundException

	{

		int v;

		Scanner sc = new Scanner(new File("network.txt"));

		v = Integer.parseInt(sc.nextLine());

		System.out.println("Number of nodes in a network: " + v);

		// System.out.println("Direct routes in a network: ");

		for (int i = 0; i < v; i++)

		{

			String source = sc.nextLine();// read source

			// System.out.println("Name of the source: "+source);

			// Declare treeSet to store adjecent nodes

			TreeSet<DistanceTo> set = new TreeSet<DistanceTo>();

			while (true)

			{

				String target_dis[] = sc.nextLine().split(",");

				if (target_dis.length == 1 || (!sc.hasNextLine()))

					break;// no target is connected than exit from loop

				int d = Integer.parseInt(target_dis[1]);

				// add DistanceTo object into set

				set.add(new DistanceTo(target_dis[0], d));

				// System.out.println(target_dis[0]+" "+d);

			}

			// add set and source to cities

			cities.put(source, set);

		}

		sc.close();// close file

	}

	void findRoutes(String starting)

	{

		String target = starting;

		// The array is defined which would contain the list of traversed

		// cities.

		ArrayList<String> visitedList = new ArrayList<String>();

		// Add DistanceTo(from, 0) to a priority queue.

		PriorityQueue<DistanceTo> p = new PriorityQueue<DistanceTo>();

		p.add(new DistanceTo(target, 0));

		// Construct a map shortestKnownDistance from city names to distances.

		Map<String, Integer> shortestKnownDistance = new HashMap<String, Integer>();

		DistanceTo smallest = null;

		// While the priority queue is not empty

		while (p.size() > 0)

		{

			// Get its smallest element.

			smallest = p.remove();

			// check if its target is not a key in shortestKnownDistance

			if (!shortestKnownDistance.containsKey(smallest.getTarget()))

			{

				visitedList.add(smallest.getTarget());

				target = smallest.getTarget();

				// Let d be the distance to that target.

				int d = smallest.getDistance();

				// Put (target, d) into shortestKnownDistance.

				shortestKnownDistance.put(target, d);

				TreeSet<DistanceTo> range = new TreeSet<DistanceTo>();

				range = cities.get(smallest.getTarget());

				// For all cities c that have a direct connection from target

				for (DistanceTo c : range)

				{

					if (!visitedList.contains(c.getTarget()))

					{

						// Add DistanceTo(c, d + distance from target to c) to the priority queue.

						DistanceTo e = new DistanceTo(c.getTarget(), d + c.getDistance());

						if (!p.contains(e))

							p.add(e);

					}

				}

			}

		}

		System.out.println("Shortest distances from " + starting + ":");

		System.out.println(shortestKnownDistance);

	}

	public static void main(String[] args) throws FileNotFoundException

	{

		AllPaths network = new AllPaths();

		// create network using input text file

		network.createGraph();

		String startingPoint;

		Scanner sc = new Scanner(System.in);

		// starting Point is the starting city input from the user

		System.out.print(" Enter the starting point:");

		startingPoint = sc.next();

		// print minimum cost from starting to all nodes in network

		network.findRoutes(startingPoint);

		sc.close();

	}

}