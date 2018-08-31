import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class R 
{
	public static void main(String[] args) throws IOException 
	{
		BufferedImage img = javax.imageio.ImageIO.read(new File("bw.jpg"));
		System.out.println(img.getWidth());
		System.out.println(img.getHeight());
		BufferedImage out = new BufferedImage(384, 288, BufferedImage.TYPE_INT_ARGB);
		double sx = img.getWidth()/384.0;
		double sy = img.getHeight()/288.0;
		double s = Math.min(sx, sy);
		Graphics g = out.getGraphics();
		boolean[] pattern = new boolean[]{
				false,false,false,true,	 //1
				true, true, true ,false, //E
				true, true, true, true,
				true, true, true, true};
		for (int y = 0; y<out.getHeight(); y++)
		{
			boolean[] line = new boolean[384];
			for (int x = 0; x<out.getWidth(); x++)
			{
				Color p = new Color(img.getRGB((int)(x*s),(int)(y*s)));
				if (p.getRed()+p.getGreen()+p.getBlue()>3*128)
				{
					line[x] = false;
					g.setColor(Color.WHITE);
				}
				else
				{
					line[x] = true;
					g.setColor(Color.BLACK);
				}
				g.drawLine(x, y, x, y);
			}
			int mine = 100;
			int minx = 12*8;
			boolean[] minp = null;
			for (int x = 12*8; x<41*8; x++)
			{
				int left_bm_w = x/8;
				for (int i = 9; i<16; i++)
					pattern[i] = line[x+i];
				int j = 9;
				while (64*bit(pattern[9])+32*bit(pattern[10])+16*bit(pattern[11])+8*bit(pattern[12])+4*bit(pattern[13])+2*bit(pattern[14])+1*bit(pattern[15])< (43-left_bm_w)*4)
				{
					pattern[j] = true;
					j++;
				}
				int e = 0;
				for (int i = 0; i<16; i++)
					e += (line[x+i]!=pattern[i]) ? 1 : 0;
				if (e<mine)
				{
					mine = e;
					minx = x;
					minp = pattern.clone();
				}
			}
			for(int i = 0; i<16; i++)
			{
				if (minp[i])
				{
					g.setColor(Color.DARK_GRAY);
				}
				else
					g.setColor(Color.CYAN);

				g.drawLine(minx+i, y, minx+i, y);
			}
		}
		
		javax.imageio.ImageIO.write(out, "png", new File("out.png"));
	}

	private static int bit(boolean b) {
		return b ? 1 : 0;
	}
}
